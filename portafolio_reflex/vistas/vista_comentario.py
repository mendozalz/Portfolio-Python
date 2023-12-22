import reflex as rx

from ..styles.colores import COLORES
from ..styles.fonst_size import SIZE


tecnologias = ["Nextjs", "Astro", "Reflex", "y Wordpress"]
tecnologias_secundarias = ["Bootraps", "Tailwind", "GSAP", "Markdown", "Web Components", "Figma", "Adobe XD", "Notion", "Airtable" ]


def  vista_comentario() -> rx.Component:
    tecnologias_str = ", ".join(tecnologias)
    return rx.box(
        rx.container(
            rx.vstack(
                rx.spacer(),
                rx.flex(
                    rx.heading(
                        rx.text("¿Hey y que técnologias manejas actualmente?"),
                        class_name="nes-balloon from-left is-dark",
                        font_size=[SIZE.MEDIANO.value, SIZE.GRANDE_x1.value, SIZE.GRANDE_x1.value, SIZE.GRANDE_x1.value, SIZE.GRANDE_x1.value]
                    ),
                    rx.span(
                        class_name="nes-bcrikko",
                    ),
                    align_items="start",
                    flex_direction="column",
                    class_name="message -left"
                ),
                rx.spacer(),
                rx.flex(
                    rx.heading(
                        rx.text("Las principales técnologias que manejo son: " + f"{tecnologias_str}"),
                        class_name="nes-balloon from-right is-dark",
                        font_size=[SIZE.MEDIANO.value, SIZE.GRANDE_x1.value, SIZE.GRANDE_x1.value, SIZE.GRANDE_x1.value, SIZE.GRANDE_x1.value]
                    ),
                    rx.span(
                        class_name="nes-bcrikko",
                    ),
                    align_items="end",
                    flex_direction="column",
                    class_name="message -right"
                ),
                rx.spacer(),
                class_name="message-list",
                height="100vh",
                ),
        ),
        class_name="nes-container is-dark",
    )
vista = vista_comentario()