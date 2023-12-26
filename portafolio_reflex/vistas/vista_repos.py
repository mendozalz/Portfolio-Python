import reflex as rx
from ..components.card import card
from ..components.repos import repos


repositorios = [
    {
        "url": "https://dub.sh/repo1-python",
        "name":"{Portfolio Astro}", 
        "descripcion":"Implementación hecha en Astro basada en el tema original de PaabloLC con cambios personalizados basado en mis necesidades."
    },
    {
        "url": "https://dub.sh/repo2-python",
        "name":"{React Estadia}", 
        "descripcion":"Proyecto React estadia como parte del aprendizaje en el uso de: React-router-dom, React Form, el uso de Watch y manipulación para impresión o descarga de documcumento PDF."
    },
    {
        "url": "https://dub.sh/repo3-python",
        "name":"{Metaverse}", 
        "descripcion":"Proyecto experimental de un metaverso creado con Next.js + Three.js experimentando el curso del mundo en 3D, las carteras digitalesy los NFT"
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
            display=["block", "block", "grid", "grid", "grid"],
        ),
    class_name="repos seccion-gsap"
    )