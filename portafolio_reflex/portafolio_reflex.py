import reflex as rx
import portafolio_reflex.styles.styles as styles

from .vistas.vista_hero import vista_hero
from .vistas.vista_repos import vista_repos
from .vistas.vista_comentario import vista_comentario
from .vistas.vista_portfolio import vista_portfolio

from .components.contenedor import contenedor
from .components.card import card
from .components.repos import repos
from portafolio_reflex.styles.colores import COLORES
from portafolio_reflex.styles.fonst_size import SIZE

def index() -> rx.Component:
    return rx.box(
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
            class_name="containerStack"
        ),
        rx.flex(
            rx.divider(variant="dashed", opacity="1", border_color="black", border_width="medium"),
            width="90%",
            margin="0 auto",
            display=["none", "none", "flex", "flex", "flex"],
        ),
        vista_comentario(),
        vista_portfolio(),
        class_name="rxBox"
        )


app = rx.App(
    stylesheets=styles.STYLESHEET,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Mi Portfolio con Python",
    description="Mi segundo portafolio y primero desarrollo web con Python puro",
    )
app.compile()