import reflex as rx

from ..styles.colores import COLORES
from ..styles.fonst_size import SIZE

def  banner() -> rx.Component:
    return rx.box(
        rx.center(
            rx.text("✨ Construido con Reflex en Python puro incluyendo el CSS ✨",
            margin="0px",
            text_align="center",
            padding_x="10px",
            font_size=["0.5em", "0.5em", SIZE.NORMAL.value, SIZE.NORMAL.value, SIZE.NORMAL.value]
            ),
        bg=COLORES.NEGRO.value,
        height=[SIZE.GRANDE.value, SIZE.GRANDE_X2.value, SIZE.GRANDE_X2.value, SIZE.GRANDE.value, SIZE.GRANDE.value],
        color=COLORES.BLANCO.value,
        )
    )
