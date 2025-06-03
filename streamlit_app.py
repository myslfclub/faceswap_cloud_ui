
import streamlit as st
import requests
import base64

st.title("🎥 Face Swap Cloud")

st.markdown("Upload a video and a face image to apply face swap.")

video_file = st.file_uploader("Upload Video File (mp4, mov)", type=["mp4", "mov"])
face_file = st.file_uploader("Upload Face Image (jpg, png)", type=["jpg", "jpeg", "png"])
resolution = st.selectbox("Output Resolution", ["720", "1080"], index=0)

if st.button("Launch FaceSwap"):
    if not video_file or not face_file:
        st.error("Please upload both a video and a face image.")
    else:
        with open("temp_video.mp4", "wb") as f:
            f.write(video_file.read())
        with open("temp_face.jpg", "wb") as f:
            f.write(face_file.read())

        files = {
            "source": ("temp_video.mp4", open("temp_video.mp4", "rb"), "video/mp4"),
            "target": ("temp_face.jpg", open("temp_face.jpg", "rb"), "image/jpeg")
        }

        try:
            url = "https://faceswap-cloud-backend-1.onrender.com/faceswap"
            response = requests.post(url, files=files)
            if response.status_code == 200:
                result = response.json()
                video_bytes = base64.b64decode(result["result_base64"])
                st.video(video_bytes)
            else:
                st.error(f"❌ Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"⚠️ Connection failed: {e}")
