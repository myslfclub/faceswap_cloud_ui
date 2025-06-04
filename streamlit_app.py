
import streamlit as st
import requests
import os

st.set_page_config(page_title="Face Swap Cloud", page_icon="🎭")

st.title("🎭 Face Swap Cloud")
st.write("Upload a video and a face image to apply face swap.")

video_file = st.file_uploader("Upload Video File (mp4, mov)", type=["mp4", "mov"])
face_image = st.file_uploader("Upload Face Image (jpg, png)", type=["jpg", "jpeg", "png"])
resolution = st.selectbox("Output Resolution", ["480", "720", "1080"])

if st.button("Launch FaceSwap") and video_file and face_image:
    backend_url = os.getenv("BACKEND_URL", "https://faceswap-cloud-backend.onrender.com/faceswap")
    api_key = os.getenv("API_KEY", "demo-key")
    files = {
        "video": (video_file.name, video_file, video_file.type),
        "face": (face_image.name, face_image, face_image.type),
    }
    data = {"resolution": resolution}
    headers = {"X-API-Key": api_key}
    response = requests.post(backend_url, files=files, data=data, headers=headers)

    if response.status_code == 200:
        with open("output.mp4", "wb") as f:
            f.write(response.content)
        st.success("✅ Face swap completed!")
        st.video("output.mp4")
    else:
        st.error(f"❌ Server error: {response.status_code} {response.text}")
