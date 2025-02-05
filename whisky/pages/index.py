import reflex as rx
import whisky.utils as utils
from whisky.components.logo import logo
from whisky.components.navbar import navbar

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
        
        rx.box(
            rx.vstack(
                navbar(),
                logo("200px", "48px"),
                margin_top="0em",                
            ),
            justify_content="center",
            align_items="center",
            padding_top="0em",
            
        ),
        
        padding_top="0em",
        size="4"
    )