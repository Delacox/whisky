import reflex as rx
import whisky.utils as utils
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
        rx.vstack(
            signup_form(),
        ),
        
    )