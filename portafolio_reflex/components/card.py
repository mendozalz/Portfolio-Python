import reflex as rx
from portafolio_reflex.styles.colores import COLORES
from portafolio_reflex.styles.fonst_size import SIZE

def  card() -> rx.Component:
    return rx.container(
        rx.box(
            rx.image(src="mendozalz_132_217.jpg", width="64px", height="106px", position="relative", z_index="1", top="25px", left="13px", transform="scale(1)" ),
            class_name= "nes-smartphone",
            transform= "scale(2)",
            top="160px",
            left=["130px", "65px", "120px", "120px", "120px"],
            z_index="1"
        ),
        rx.box(
            rx.vstack(
                rx.link(
                    rx.span(
                    class_name="nes-icon whatsapp is-medium", 
                    position="absolute", 
                    top="20px", 
                    margin="0px !important"),
                    href="https://api.whatsapp.com/send?phone=5730224082997&text=Hola%20Lenin%20he%20visto%20tu%20portafolio%20y%20quisiera%20hablar%20contigo,%20tienes%20tiempo%20disponible%20para%20platicar?",
                    is_external=True
                ),
                rx.span("Tlf:"),
                rx.span("+573022408297"),
                rx.text("Soy un apasionado desarrollador web que disfruta experimentando con diversas tecnologías", line_height="20px", font_size=SIZE.PEQUENO.value),
                padding_top="75px", 
                font_size=SIZE.INTERMEDIO.value,
                align_items="start"
            ),
            class_name="nes-container is-rounded",
            position="relative",
            color=COLORES.BLANCO.value,
            width="210px",
            height="300px",
            padding="10px !important",
            margin_top="130px !important",
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