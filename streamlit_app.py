
import streamlit as st
import requests
from PIL import Image
import io
import base64

st.set_page_config(page_title="FaceSwap Cloud", layout="centered")
st.title("🤖 FaceSwap Cloud UI")

st.write("Téléversez deux images : visage source et visage cible")

source_file = st.file_uploader("Source (visage à copier)", type=["jpg", "jpeg", "png"])
target_file = st.file_uploader("Target (visage à recevoir)", type=["jpg", "jpeg", "png"])

if st.button("Lancer le FaceSwap") and source_file and target_file:
    with st.spinner("Traitement en cours..."):
        files = {
    "source": open(video_path, "rb"),   # le fichier vidéo
    "target": open(face_path, "rb")     # l’image du visage
}
        try:
            # Remplace cette URL par celle de ton backend Render
            url = "https://faceswap_cloud_backend.onrender.com/faceswap"
            response = requests.post(url, files=files)
            response.raise_for_status()
            result = response.json()["result_base64"]
            image_bytes = base64.b64decode(result)
            st.image(Image.open(io.BytesIO(image_bytes)), caption="Résultat FaceSwap", use_column_width=True)
        except Exception as e:
            st.error(f"Erreur : {e}")
