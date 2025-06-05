import streamlit as st
import requests

BACKEND_URL = "https://faceswap-cloud-backend.onrender.com/faceswap"

st.title("FaceSwap UI")

uploaded_video = st.file_uploader("Upload your video", type=["mp4"])
uploaded_face = st.file_uploader("Upload the face image", type=["jpg", "jpeg", "png"])
resolution = st.selectbox("Choose resolution", ["480p", "720p", "1080p"])

if st.button("Swap Face"):
    if uploaded_video and uploaded_face:
        with st.spinner("Processing..."):
            files = {
                "video": uploaded_video,
                "face": uploaded_face,
            }
            data = {"resolution": resolution}
            response = requests.post(BACKEND_URL, files=files, data=data)
            if response.status_code == 200:
                st.video(response.content)
            else:
                st.error("Failed to process video")
    else:
        st.warning("Please upload both video and face image.")
