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
}
