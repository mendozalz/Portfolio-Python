import reflex as rx
from ..components.contenedor import contenedor
from ..styles.colores import COLORES
from portafolio_reflex.components.reloj import reloj
from portafolio_reflex.components.logo import logo
from portafolio_reflex.components.banner import banner
from portafolio_reflex.components.navidad import navidad


def  vista_hero() -> rx.Component:
    return rx.container(
        rx.box(
            rx.hstack(
                logo(),
                reloj(),
                padding_y="30px"
            ),
            contenedor(),
            rx.box(
                rx.span("Hola"),
                rx.text(
                    "Mi nombre es:", 
                    rx.span("Lenin Mendoza", color= COLORES.TERCIARIO.value),
                    margin="0px", 
                    ),
                rx.text(
                    "Front-End",
                    rx.span(" Developer", color= COLORES.TERCIARIO.value),
                ),
                aling_items = "start",
                margin_top="10px"
            ),
        height="100vh",
        #z_index=-1
        ),
    class_name="hero seccion-gsap"
    )