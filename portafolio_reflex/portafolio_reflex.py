import reflex as rx
import portafolio_reflex.styles.styles as styles

from .vistas.vista_hero import vista_hero
from .vistas.vista_repos import vista_repos
from .vistas.vista_comentario import vista_comentario
from .vistas.vista_portfolio import vista_portfolio

from .components.contenedor import contenedor
from portafolio_reflex.components.banner import banner
from portafolio_reflex.components.navidad import navidad
from .components.card import card
from .components.repos import repos
from portafolio_reflex.styles.colores import COLORES
from portafolio_reflex.styles.fonst_size import SIZE

def index() -> rx.Component:
    return rx.box(
        banner(),
        navidad(),
        rx.container(
            rx.hstack(
                rx.vstack(
                    vista_hero(),
                    vista_repos(),
                    padding_bottom= SIZE.GRANDE.value,
                    class_name="verticalStack"
                ), 
            width="auto",
            display=["block", "block", "flex", "flex", "flex"],
            class_name="horizontalStack"    
            ),
            class_name="containerStack hero"
        ),
        rx.flex(
            rx.divider(variant="dashed", opacity="1", border_color="black", border_width="medium"),
            width="90%",
            margin="0 auto",
            display=["none", "none", "flex", "flex", "flex"],
        ),
        vista_comentario(),
        vista_portfolio(),
        class_name="rxBox",
        )


app = rx.App(
    stylesheets=styles.STYLESHEET,
    style=styles.BASE_STYLE,
    head_components=[rx.script(src="https://cdn.jsdelivr.net/gh/studio-freight/lenis@1.0.29/bundled/lenis.min.js"),
    rx.script(src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.4/gsap.min.js"),
    rx.script(src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.4/ScrollTrigger.min.js"),
            ]
)
app.add_page(
    index,
    title="Mi Portfolio con Python",
    description="Mi segundo portafolio y primero desarrollo web con Python puro",
    )
app.compile()