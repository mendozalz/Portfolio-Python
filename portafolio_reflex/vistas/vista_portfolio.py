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
                        rx.text("1Body of the Card Component", class_name="rxCardText"),
                        header=rx.heading("Header", size="lg"),
                        footer=rx.heading("Footer", size="sm"),
                        height="100%",
                        transition= "all 0.3s ease-in-out",
                        _hover={
                            "box_shadow": f"1px 1px {COLORES.NES.value}, 6px 6px {COLORES.NES.value}, 3px 3px {COLORES.NES.value}",
                            "transform": "translateX(-3px)",
                        },
                        padding_y="0px"
                        ),
                    href="#",
                    is_external=True
                    ),row_span=2, 
                    col_span=1,
                    margin_bottom=["10px", "0px", "0px", "0px", "0px"]
                    ),
                rx.grid_item(
                    rx.link(
                        rx.card(
                        rx.text("2Body of the Card Component"),
                        header=rx.heading("Header", size="lg"),
                        footer=rx.heading("Footer", size="sm"),
                        height="100%",
                        transition= "all 0.3s ease-in-out",
                        _hover={
                            "box_shadow": f"1px 1px {COLORES.NES.value}, 6px 6px {COLORES.NES.value}, 3px 3px {COLORES.NES.value}",
                            "transform": "translateX(-3px)",
                        }
                        ),
                    href="#",
                    is_external=True
                    ),
                    col_span=2,
                    margin_bottom=["10px", "0px", "0px", "0px", "0px"]
                    ),
                rx.grid_item(
                    rx.link(
                        rx.card(
                        rx.text("3Body of the Card Component"),
                        header=rx.heading("Header", size="lg"),
                        footer=rx.heading("Footer", size="sm"),
                        height="100%",
                        transition= "all 0.3s ease-in-out",
                        _hover={
                            "box_shadow": f"1px 1px {COLORES.NES.value}, 6px 6px {COLORES.NES.value}, 3px 3px {COLORES.NES.value}",
                            "transform": "translateX(-3px)",
                        }
                        ),
                    href="#",
                    is_external=True
                    ),
                    col_span=2,
                    margin_bottom=["10px", "0px", "0px", "0px", "0px"]
                    ),
                rx.grid_item(
                    rx.link(
                        rx.card(
                        rx.text("4Body of the Card Component"),
                        header=rx.heading("Header", size="lg"),
                        footer=rx.heading("Footer", size="sm"),
                        height="100%",
                        transition= "all 0.3s ease-in-out",
                        _hover={
                            "box_shadow": f"1px 1px {COLORES.NES.value}, 6px 6px {COLORES.NES.value}, 3px 3px {COLORES.NES.value}",
                            "transform": "translateX(-3px)",
                        }
                        ),
                    href="#",
                    is_external=True
                    ),
                    col_span=3,
                    display=["none", "grid", "grid", "grid", "grid"]
                    ),
                rx.grid_item(
                    rx.link(
                        rx.card(
                        rx.text("5Body of the Card Component"),
                        header=rx.heading("Header", size="lg"),
                        footer=rx.heading("Footer", size="sm"),
                        transition= "all 0.3s ease-in-out",
                        _hover={
                            "box_shadow": f"1px 1px {COLORES.NES.value}, 6px 6px {COLORES.NES.value}, 3px 3px {COLORES.NES.value}",
                            "transform": "translateX(-3px)",
                        }
                        ),
                    href="#",
                    is_external=True
                    ),
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
    )