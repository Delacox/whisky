import reflex as rx
import whisky.utils as utils
from whisky.components.login_form import login_form
@rx.page(
    title = utils.login_title,
    description = utils.login_description,
    image = utils.preview,
    meta = utils.login_meta,
)


def login() -> rx.Component:
    # Devolvemos contenedor principal de la web
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            login_form(),
        ),
        
    )