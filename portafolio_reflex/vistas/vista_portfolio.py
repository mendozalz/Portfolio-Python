import reflex as rx
from ..components.footer import footer
from ..styles.colores import COLORES

def  vista_portfolio() -> rx.Component:
    return rx.box(
            rx.container(
            rx.vstack(
            rx.box(rx.text("{Mis ultimos despliegues}"), align_items="start", width="100%"),
            rx.box(
                rx.responsive_grid(
                rx.grid_item(
                    rx.link(
                        rx.card(
                        rx.text("API Poemas AWS Lambda...", class_name="rxCardText"),
                        header=rx.heading("Poemas", size="lg"),
                        footer=rx.heading("AWS, API OpenAI", size="sm"),
                        height="100%",
                        transition= "all 0.3s ease-in-out",
                        _hover={
                            "box_shadow": f"1px 1px {COLORES.NES.value}, 6px 6px {COLORES.NES.value}, 3px 3px {COLORES.NES.value}",
                            "transform": "translateX(-3px)",
                        },
                        padding_y="0px"
                        ),
                    href="https://dub.sh/api-poemas-python",
                    is_external=True
                    ),
                    row_span=2, 
                    col_span=1,
                    margin_bottom=["10px", "0px", "0px", "0px", "0px"]
                    ),
                rx.grid_item(
                    rx.link(
                        rx.card(
                        rx.text("Metaverso en producción..."),
                        header=rx.heading("Metaverse", size="lg"),
                        footer=rx.heading("Next.js, Three.js", size="sm"),
                        height="100%",
                        transition= "all 0.3s ease-in-out",
                        _hover={
                            "box_shadow": f"1px 1px {COLORES.NES.value}, 6px 6px {COLORES.NES.value}, 3px 3px {COLORES.NES.value}",
                            "transform": "translateX(-3px)",
                        }
                        ),
                    href="https://dub.sh/metaverse-python",
                    is_external=True
                    ),
                    row_span=0,
                    col_span=2,
                    margin_bottom=["10px", "0px", "0px", "0px", "0px"]
                    ),
                rx.grid_item(
                    rx.link(
                        rx.card(
                        rx.text("Simulación de recorrido de 360 grados..."),
                        header=rx.heading("Recorrido 360°", size="lg"),
                        footer=rx.heading("Marzipano, JS, HTML, CSS", size="sm"),
                        height="100%",
                        transition= "all 0.3s ease-in-out",
                        _hover={
                            "box_shadow": f"1px 1px {COLORES.NES.value}, 6px 6px {COLORES.NES.value}, 3px 3px {COLORES.NES.value}",
                            "transform": "translateX(-3px)",
                        }
                        ),
                    href="https://dub.sh/marzipano-python",
                    is_external=True
                    ),
                    row_span=0,
                    col_span=2,
                    margin_bottom=["10px", "0px", "0px", "0px", "0px"]
                    ),
                rx.grid_item(
                    rx.link(
                        rx.card(
                        rx.text("Mi primer portafolio con excelente redimiento en Lighthouse..."),
                        header=rx.heading("Portafolio principal", size="lg"),
                        footer=rx.heading("Astro.js", size="sm"),
                        height="100%",
                        transition= "all 0.3s ease-in-out",
                        _hover={
                            "box_shadow": f"1px 1px {COLORES.NES.value}, 6px 6px {COLORES.NES.value}, 3px 3px {COLORES.NES.value}",
                            "transform": "translateX(-3px)",
                        }
                        ),
                    href="https://dub.sh/vercel-python",
                    is_external=True
                    ),
                    row_span=0,
                    col_span=3,
                    display=["none", "grid", "grid", "grid", "grid"]
                    ),
                rx.grid_item(
                    rx.link(
                        rx.card(
                        rx.text("FrontEnd propuesta Meet de reuniones virtuales..."),
                        header=rx.heading("GC Meet", size="lg"),
                        footer=rx.heading("Angular 16", size="sm"),
                        transition= "all 0.3s ease-in-out",
                        height="100%",
                        _hover={
                            "box_shadow": f"1px 1px {COLORES.NES.value}, 6px 6px {COLORES.NES.value}, 3px 3px {COLORES.NES.value}",
                            "transform": "translateX(-3px)",
                        }
                        ),
                    href="https://dub.sh/meet-python",
                    is_external=True
                    ),
                    row_span=0,
                    col_span=1,
                    display=["none", "grid", "grid", "grid", "grid"]
                    ),
                template_rows="repeat(2, 1fr)",
                template_columns="repeat(5, 1fr)",
                display=["columns", "grid", "grid", "grid", "grid"],
                h="100%",
                width="100%",
                gap=2,
            ),
            class_name="rxBoxPortfolio"
            ),
            ),
            padding="20px",
            height=["100%", "calc( 100vh - 8em)", "calc( 100vh - 8em)", "calc( 100vh - 8em)", "calc( 100vh - 8em)"],
            display="flex",
            align_items="center"
            ),
    footer(),
    bg=COLORES.PRIMARIO.value,
    position="relative",
    class_name="portfolio seccion-gsap",
    )