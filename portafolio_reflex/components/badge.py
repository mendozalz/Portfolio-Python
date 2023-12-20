import reflex as rx

def  badge(nombre:str) -> rx.Component:
    return rx.container(
            rx.span(
                nombre,
                padding="2px 15px",
                background_color="#FF4F01",
                box_shadow="0 0.5em #FF4F01, 0 -0.5em #FF4F01, 0.5em 0 #FF4F01, -0.5em 0 #FF4F01;"
            ),
            class_name="nes-badge"
    )