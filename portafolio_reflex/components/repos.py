import reflex as rx
from portafolio_reflex.styles.colores import COLORES
from portafolio_reflex.styles.fonst_size import SIZE

def repos(repos_list: list) -> rx.Component:
    repos_components = [
        rx.link(
            rx.container(
            rx.text(
                f"{repo['name']}",
                bg=COLORES.PRIMARIO.value,
                class_name="title"
            ),
            rx.text(f"{repo['descripcion']}"),
            class_name="nes-container is-rounded with-title",
            border_image_outset="inherit !important",
            margin="0px !important"
        ),
        _hover={
        "text_decoration": "none",
        "color": "gray !important",
        "opacity": "0.6"
        },
        href=repo["url"],
        is_external= True
        )
        for repo in repos_list
    ]

    return rx.vstack(
        rx.box(rx.text("{Mis ultimos repos}"), width="100%"),
        *repos_components, 
        gap="20px", 
        height="100%", 
        justify_content="center")