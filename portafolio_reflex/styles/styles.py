import reflex as rx

from .fonst_size import FONT,SIZE
from .colores import COLORES


STYLESHEET = [
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap"
]

BASE_STYLE = {
    "font_family": FONT.DEFAULT.value,
    "background": COLORES.PRIMARIO.value,
    "font_size":  SIZE.NORMAL.value,
    "border_image_outset": "inherit",
     rx.Link: {
        "text_decoration": "none",
        "_hover": {
            "text_decoration": "none",
            "opacity": "0.6"
        }
    },

    # Navidad

    "svg": {
    "max_height":["12vh", "20vh", "20vh", "20vh", "20vh" ],
    "width": "auto",
    "overflow": "visible",
    },
    "path": {
    "fill": "#379157",
    "stroke": "#379157",
    "stroke_width": "0.2",
    "transform": "scale(0)",
    "transform_origin": "50%, 50%",
    "animation": "star 8s ease-in-out infinite",
    "animation_delay": "calc(var(--no) * 0.025s)",
    "transform_box": "fill-box"
    },
"@keyframes star": {
  "0%": {
    "transform": "scale(0)",
    "animation_timing_function": "cubic-bezier(0.74, 1.72, 0.57, 1.01)",
  },
  "10%": {
    "transform": "scale(1)",
  },
  "65%": {
    "transform": "translateY(0px) scale(1)",
  },
  "75%": {
    "transform": "translateY(50px) scale(0)",
  },
  "100%": {
    "transform": "translateY(0px) scale(0)",
  }
},

# Feliz Navidad

"svg.feliz": {
  "max_height":["4vh", "20vh", "20vh", "20vh", "20vh" ],
  "width": "auto",
},



"@keyframes blink-caret": {

    "0%": {
        "border_color": "transparent",
    },

    "50%": {
        "border_color": "#ffffff"
    }
},


# Lenis

"html.lenis": {
  "height": "auto"
},

".lenis.lenis-smooth": {
  "scroll-behavior": "auto"
},

".lenis.lenis-smooth [data-lenis-prevent]": {
  "overscroll-behavior": "contain"
},

".lenis.lenis-stopped": {
  "overflow": "hidden"
},

".lenis.lenis-scrolling iframe": {
  "pointer-events": "none"
}


}
