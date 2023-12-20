import reflex as rx
from ..components.card import card
from ..components.repos import repos


repositorios = [
    {
        "url": "https://github.com/mendozalz?tab=repositories",
        "name":"{Lenin 1}", 
        "descripcion":"Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500"
    },
    {
        "url": "https://github.com/mendozalz?tab=repositories",
        "name":"{Lenin 2}", 
        "descripcion":"Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500"
    },
    {
        "url": "https://github.com/mendozalz?tab=repositories",
        "name":"{Lenin 3}", 
        "descripcion":"Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500"
    },
]

def  vista_repos() -> rx.Component:
    return rx.container(
        rx.responsive_grid(
            rx.grid_item(
                card(), 
                row_span=3, 
                col_span=1,
                align_items="center",
                height="100%"
                ),
            # 
            rx.grid_item(
                repos(repositorios),
                col_span=1,
                align_items="center",
                height=["100%", "100vh", "100vh", "100vh", "100vh"]
                ),
            template_rows="repeat(3, auto)",
            template_columns="300px 1fr",
            align_items="center",
            width="100%",
            #height="100%",
            display=["block", "block", "grid", "grid", "grid"],
        ),
    )