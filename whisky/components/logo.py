import reflex as rx

def logo(width:str = "300px", font_size: str = "32px") -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.image(
                src="/logo.png",
                width = width,
            ),
            rx.text(
                "DRAW OF DESTINY",
                font_family = "Playfair Display",
                font_size = font_size,
                color = rx.color_mode_cond(
                    light="black",
                    dark="white",
                ),
            ),
            align="center",
            justify="center",
            spacing="4",
        ),
        justify_content="center",
        width="100%",
    )