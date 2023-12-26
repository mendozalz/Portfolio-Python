const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  direction: "vertical",
  gestureOrientation: "vertical",
  smoothWheel: true,
  smoothTouch: true,
  wheelMultiplier: 1,
  touchMultiplier: 2,
  infinite: false,
});

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}

requestAnimationFrame(raf);

lenis.on("scroll", ScrollTrigger.update);

gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
});

gsap.ticker.lagSmoothing(0);

gsap.registerPlugin(ScrollTrigger);

gsap.to(".hero", {
  yPercent: 100,
  ease: "none",
  scrollTrigger: {
    trigger: ".comentario",
    start: "top bottom",
    end: "top top",
    scrub: true,
  },
});

gsap.to(".comentario", {
  yPercent: 100,
  ease: "none",
  scrollTrigger: {
    trigger: ".portfolio",
    start: "top bottom",
    end: "top top",
    scrub: true,
  },
});
