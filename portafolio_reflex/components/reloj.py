import reflex as rx
from portafolio_reflex.styles.colores import COLORES
from portafolio_reflex.styles.fonst_size import SIZE

def  reloj() -> rx.Component:
    return rx.center(
        rx.text(
        class_name="fecha_actual",
        font_size= ["1.3em", SIZE.MEDIANO.value, SIZE.GRANDE.value, SIZE.GRANDE_X2.value, ],
        text_align="center",
        padding_top="15px",
        opacity="0.07"
        ),
        rx.script(src="/js/hora.js")
    )