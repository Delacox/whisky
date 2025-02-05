import reflex as rx
import whisky.utils as utils

# Definimos la interfaz
# Lo que creemos con el decorador rx.page sera una pagina de la web
@rx.page(
    title = utils.index_title,
    description = utils.index_description,
    image = utils.preview,
    meta = utils.index_meta,
)


def index() -> rx.Component:
    # Devolvemos contenedor principal de la web
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.link(rx.button("Login"), href="/login"),
            rx.link(rx.button("Registro"), href="/signup"),
        ),
        
    )