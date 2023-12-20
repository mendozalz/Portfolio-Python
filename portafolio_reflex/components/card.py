import reflex as rx
from portafolio_reflex.styles.colores import COLORES
from portafolio_reflex.styles.fonst_size import SIZE

def  card() -> rx.Component:
    return rx.container(
        rx.box(
            rx.image(src="mendozalz_132_217.jpg", width="64px", height="106px", position="relative", z_index="1", top="25px", left="13px", transform="scale(1)" ),
            class_name= "nes-smartphone",
            transform= "scale(2)",
            top="120px",
            left=["135px", "65px", "65px", "105px", "105px"],
            z_index="1"
        ),
        rx.box(
            rx.vstack(
                rx.span("Tlf:"),
                rx.span("+573022408297"),
                rx.text("Soy un apasionado desarrollador web que disfruta experimentando con diversas tecnologías", line_height="20px", font_size=SIZE.PEQUENO.value),
                top="190px", 
                font_size=SIZE.INTERMEDIO.value,
                position="relative",
                align_items="start"
            ),
            class_name="nes-container is-rounded",
            color=COLORES.BLANCO.value,
            width="210px",
            height="400px",
            padding="10px !important",
            background=COLORES.SECUNDARY.value
        ),
        rx.box(
            rx.divider(
                    variant="dashed", orientation="vertical", opacity="1", border_color="black", border_width="medium"
                ),
                height="100%",
                position= "absolute",
                top= "6%",
                margin_left=["250px", "250px", "265px", "265px", "265px"],
                display=["none", "none", "flex", "flex", "flex"],
        ),
        rx.box(
            class_name="nes-jp-logo",
            position="absolute",
            margin_left="235px",
            bottom="-38px",
            z_index="1",
            display=["none", "none", "flex", "flex", "flex"],
        ),
        height=["100%", "70vh", "100vh", "100vh", "100vh", ],
        width="100%",
        padding=["30px", "0", "0", "0", "0"],
        position="relative",
        display= "flex",
        flex_direction= "column",
        justify_content= "center"
        
    )