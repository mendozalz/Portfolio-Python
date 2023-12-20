import reflex as rx
from portafolio_reflex.styles.colores import COLORES
from portafolio_reflex.styles.fonst_size import SIZE

def  contenedor() -> rx.Component:
    return rx.container(
        rx.box(
            rx.text("2023", class_name="title"),
            rx.text("Bienvenido a mi portafolio hecho en Python puro aunque no lo parezca",
            rx.span(".", color= COLORES.TERCIARIO.value),
            font_size= [SIZE.MEDIANO.value, SIZE.GRANDE.value, SIZE.GRANDE.value, SIZE.GRANDE.value, SIZE.GRANDE.value]
            ),
        class_name = "nes-container is-dark with-title",
        ),
        padding = "0px",
        margin="auto",
        class_name="contenedorBienvenido"
    )