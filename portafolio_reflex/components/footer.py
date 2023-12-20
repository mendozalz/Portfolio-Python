import reflex as rx
from portafolio_reflex.styles.colores import COLORES
from portafolio_reflex.styles.fonst_size import SIZE

def footer() -> rx.Component:
    # Lista de diccionarios que contiene la información de cada imagen y enlace
    images_links_data = [
        {"src": "/Linkeding.png", "width": "30px", "height": "auto", "filter": "invert(0%) sepia(25%) saturate(0%) hue-rotate(61deg) brightness(104%) contrast(100%)", "href": "#", "is_external": True},
        {"src": "/GitHub.png", "width": "30px", "height": "auto", "filter": "invert(41%) sepia(0%) saturate(1%) hue-rotate(87deg) brightness(99%) contrast(97%)", "href": "#", "is_external": True},
        {"src": "/notion.png", "width": "30px", "height": "auto", "filter": "invert(41%) sepia(0%) saturate(1%) hue-rotate(87deg) brightness(99%) contrast(97%)", "href": "#", "is_external": True}
    ]

    # Crear dinámicamente las imágenes y enlaces usando la información de la lista
    images_links = [rx.link(rx.image(src=image["src"], width=image["width"], height=image["height"], filter=image["filter"]), href=image["href"], is_external=image["is_external"]) for image in images_links_data]

    return rx.box(
        rx.container(
            rx.center(
                rx.vstack(
                    rx.text("Lenin Mendoza | Python - 2023", font_size=SIZE.NORMAL.value, color=COLORES.BLANCO.value, margin_bottom="10px", text_align="center"),
                    rx.hstack(*images_links, gap=4, margin_bottom="10px !important"),  
                    rx.text("Colombia/Medellín", font_size=SIZE.PEQUENO.value, color=COLORES.BLANCO.value)
                )
            )
        ),
        bg=COLORES.NES.value,
        width="100vw",
        height=SIZE.GRANDE_X5.value,
        display="grid",
        align_items="center"
    )
