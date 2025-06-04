import streamlit as st
import requests

st.title("🎭 Face Swap Cloud")

video_file = st.file_uploader("Upload Video File", type=["mp4", "mov"])
face_file = st.file_uploader("Upload Face Image", type=["jpg", "jpeg", "png"])
resolution = st.selectbox("Output Resolution", ["720", "1080"])
if st.button("Launch FaceSwap"):
    if video_file and face_file:
        files = {
            "video": (video_file.name, video_file, "video/mp4"),
            "face": (face_file.name, face_file, "image/jpeg"),
        }
        data = {"resolution": resolution}
        headers = {"X-API-Key": st.secrets["API_KEY"]}
        response = requests.post(st.secrets["BACKEND_URL"], files=files, data=data, headers=headers)
        st.write("✅ Response:", response.json())
    else:
        st.error("Please upload both a video and a face image.")
