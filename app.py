import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "https://faceswap-cloud-backend-1.onrender.com/faceswap")
API_KEY = os.getenv("API_KEY", "demo-key")

st.title("🎭 Face Swap Cloud")

uploaded_video = st.file_uploader("Upload Video File (mp4, mov)", type=["mp4", "mov", "mpeg4"])
uploaded_image = st.file_uploader("Upload Face Image (jpg, png)", type=["jpg", "jpeg", "png"])
resolution = st.selectbox("Output Resolution", options=["480", "720", "1080"])

if st.button("Launch FaceSwap"):
    if uploaded_video and uploaded_image:
        files = {
            "source": ("video.mp4", uploaded_video, uploaded_video.type),
            "target": ("image.jpg", uploaded_image, uploaded_image.type),
        }
        data = {"resolution": resolution}
        try:
            with st.spinner("Swapping faces..."):
                response = requests.post(BACKEND_URL, files=files, data=data, headers={"x-api-key": API_KEY})
            if response.status_code == 200:
                output_path = "/tmp/output.mp4"
                with open(output_path, "wb") as f:
                    f.write(response.content)
                st.success("✅ Face swap completed!")
                st.video(output_path)
            else:
                st.error(f"❌ Server error: {response.status_code}\n{response.text}")
        except Exception as e:
            st.error(f"Exception occurred: {e}")
    else:
        st.warning("Please upload both video and face image.")
