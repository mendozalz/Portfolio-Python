import reflex as rx
from portafolio_reflex.styles.colores import COLORES
from portafolio_reflex.styles.fonst_size import SIZE

def  contenedor() -> rx.Component:
    return rx.container(
        rx.box(
            rx.text("Python - 2023", class_name="title", font_size=SIZE.INTERMEDIO.value),
            rx.text("Bienvenido a mi portafolio Web",
            rx.span(".", color= COLORES.TERCIARIO.value),
            font_size= [SIZE.MEDIANO.value, SIZE.GRANDE_x1.value, SIZE.GRANDE_x1.value, SIZE.GRANDE_x1.value, SIZE.GRANDE_x1.value]
            ),
        class_name = "nes-container is-dark with-title",
        ),
        padding = "0px",
        margin="auto",
        class_name="contenedorBienvenido"
    )