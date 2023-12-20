import reflex as rx
from portafolio_reflex.styles.colores import COLORES
from portafolio_reflex.styles.fonst_size import SIZE

def  logo() -> rx.Component:
    return rx.box(
        rx.image(
            src="/logo_negro.png", width="250px", height="auto"
        )
    )