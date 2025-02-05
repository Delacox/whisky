import reflex as rx
import whisky.utils as utils
from whisky.components.navbar import navbar
from whisky.components.signup_form import signup_form

@rx.page(
    title = utils.signup_title,
    description = utils.signup_description,
    image = utils.preview,
    meta = utils.signup_meta,
)


def signup() -> rx.Component:
    # Devolvemos contenedor principal de la web
    return rx.container(
        rx.color_mode.button(position="top-right"),
        navbar(),
        rx.vstack(
            signup_form(),
            padding_top="4em",
        ),
        
        padding_top="0em",
        size="4"
    )