import reflex as rx
from rxconfig import config
from whisky.styles.global_styles import global_style
from whisky.styles.component_styles import component_styles
from whisky.styles.theme import theme
from whisky.pages.index import index
from whisky.pages.login import login
from whisky.pages.signup import signup

# Estado de la aplicacion
class State(rx.State):
    """The app state."""

    ...


# Combinar estilos
all_styles = {
    **global_style,
    **component_styles,
}

# Configuracion de la aplicacion
app = rx.App(
    stylesheets=["https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900&display=swap"],
    
    style=all_styles,
    theme=theme,
)
