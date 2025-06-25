import streamlit as st
from PIL import Image
from urllib.request import urlopen
from PIL import Image

# Configuración general de la página
st.set_page_config(
    page_title="César Bueno - Portafolio",
    page_icon="🖋️",
    layout="centered"
)

# Estilos personalizados: fondo azul oscuro y letras blancas
st.markdown(
    """
    <style>
    body {
        background-color: #0F1C2E;
        color: white;
    }
    .stApp {
        background-color: #0F1C2E;
        color: white;
    }
    h1, h2, h3, h4 {
        color: white;
    }
    a {
        color: #1FA2FF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Imagen de perfil
image_url = "https://raw.githubusercontent.com/CesarGBG/portafoliocesar/1471126e65e63d9de60734cffd6d9893fe28bfb0/foto.jpg"
imagen = Image.open(urlopen(image_url))
st.image(imagen, caption="César Bueno", use_column_width=True)

# Título y descripción
st.title("Hola, soy César Bueno")
st.subheader("Estudiante de Publicidad | PUCP")

st.write("""
Soy una persona entusiasta, analítica y creativa, interesada en el mundo del marketing y diseño.  
Siempre dispuesto a aceptar nuevos retos y adquirir conocimiento.
""")

# Habilidades
st.header("🛠️ Habilidades")
st.write("""
- ✍️ Redacción  
- 🎨 Dibujo  
- 🖼️ Edición fotográfica  
- 🎬 Edición de video
""")

# Contacto
st.header("📬 Contacto")
st.write("¿Quieres saber más o colaborar?")
st.markdown("📧 [gianfrancobueno212@gmail.com](mailto:gianfrancobueno212@gmail.com)")




