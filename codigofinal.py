# -*- coding: utf-8 -*-
"""codigofinal

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13rzUyIdfb2kWsJO2nEZQLLjVU2tfqCsB
"""

import streamlit as st
from PIL import Image
import os

# 🎨 Fondo con imagen clara
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.1)),
                url("https://i.imgur.com/pGcYBAT.jpeg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    color: black;
}
h1, h2, h3, h4, h5, h6, p {
    color: black !important;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# 🛠 Configuración de la página
st.set_page_config(page_title="Portafolio de Gabriela", page_icon="✨", layout="wide")

# 📷 Foto de perfil
try:
    img = Image.open("foto_de_perfil1.jpg")
    st.image(img, width=200)
except FileNotFoundError:
    st.warning("No se encontró 'foto_de_perfil1.jpg'. Asegúrate de que esté en la misma carpeta.")

# 👋 Presentación
st.title("Gabriela del Castillo")
st.subheader("Estudiante de Comunicación Audiovisual")

st.markdown("""
¡Hola! Bienvenida/o a mi portafolio interactivo.

Soy estudiante y me encuentro actualmente en el cuarto de año de carrera de Audiovisuales en la PUCP. Me gusta el cine y me he enfocado en el estudio del lenguaje audiovisual y la narrativa. Este portafolio reúne algunos proyectos audiovisuales y fotografías parte de mi desarrollo académico y artístico. Aquí podrás ver algunos de mis trabajos, donde exploro mi visión, mis referentes y mi estilo narrativo, además de cómo contactarme.
""")

st.markdown("---")

# 🚀 Proyectos Destacados
st.header("Proyectos Destacados")

col1, col2 = st.columns(2)

# 📸 Galería de fotografía desde archivos locales
with col1:
    st.subheader("Fotografía")
    st.markdown("Lo cotidiano, lo simbólico, lo invisible.")

    # Lista de archivos locales
    fotos = ["nicole_pirueta.jpg", "monito_abuelo.jpg", "ojos_candidos.jpg", "nicole_sentada.jpg", "monito_enojado.jpg", "the_faites.jpg", "luz_nicole.jpg", "nicole_conversando.jpg"]

    for i in range(0, len(fotos), 3):
        galeria_cols = st.columns(3)
        for j, foto in enumerate(fotos[i:i+3]):
            with galeria_cols[j]:
                if os.path.exists(foto):
                    st.image(foto, use_container_width=True)
                else:
                    st.error(f"No se encontró la imagen: {foto}")

# 🎬 Proyecto en video (YouTube)
with col2:
    st.subheader("Smartest women")
    st.markdown("Videoclip con imágenes fijas: Un trabajo académico para un curso de carrera.")

    st.video("https://www.youtube.com/watch?v=d9ekOsPTmNo")
    st.markdown("[Ver en YouTube](https://www.youtube.com/watch?v=d9ekOsPTmNo)")

st.markdown("---")

# 🛠️ Habilidades
st.header("Habilidades")
st.markdown("""
- **Lenguas:** Inglés avanzado, Francés básico
- **Lenguajes:** Python, Excel
- **Creatividad:** Storytelling, escritura narrativa
- **Otras:** Producción audiovisual, escritura académica
""")

st.markdown("---")

# 📫 Contacto
st.header("📫 Contacto")
st.markdown("- 📧 Email: gabdelca1@gmail.com")

st.markdown("> Gracias por visitar mi portafolio.")