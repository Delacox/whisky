import reflex as rx

# Datos comunes

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang = 'es'") # Idioma de la pagina

preview = "preview.jpg" # Imagen de previsualizacion

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "keywords", "content": "whisky,blog,informacion,bebida,alcohol"},
    {"name": "robots", "content": "index, follow"},
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
]


# Index
index_title = "Whisky" # Titulo de la pagina
index_description = "Informacion sobre whisky" # Descripcion de la pagina
index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# Signup
signup_title = "Registro | Whisky"
signup_description = "Blog informativo sobre whisky"
signup_meta = [
    {"name": "og:title", "content": signup_title},
    {"name": "og:description", "content": signup_description},
]
signup_meta.extend(_meta)

# Login
login_title = "Login | Whisky"
login_description = "Blog informativo sobre whisky"
login_meta = [
    {"name": "og:title", "content": login_title},
    {"name": "og:description", "content": login_description},
]
login_meta.extend(_meta)