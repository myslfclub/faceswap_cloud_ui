import streamlit as st
import requests

st.set_page_config(page_title="Face Swap Cloud", layout="centered")

st.title("🎥 Face Swap Cloud")
st.write("Upload a video and a face image to apply face swap.")

# Upload video
video_file = st.file_uploader("Upload Video File (mp4, mov)", type=["mp4", "mov", "mpeg4"])
# Upload image
image_file = st.file_uploader("Upload Face Image (jpg, png)", type=["jpg", "jpeg", "png"])
# Select resolution
resolution = st.selectbox("Output Resolution", options=["480", "720", "1080"], index=1)

if st.button("Launch FaceSwap"):
    if video_file and image_file:
        with st.spinner("Processing..."):
            files = {
                "source": (image_file.name, image_file, "image/jpeg"),
                "target": (video_file.name, video_file, "video/mp4")
            }
            data = {"resolution": resolution}
            try:
                response = requests.post(
                    "https://faceswap-cloud-backend-1.onrender.com/faceswap",
                    files=files,
                    data=data
                )
                if response.status_code == 200:
                    st.success("✅ Face swap completed!")
                    st.video(response.content)
                else:
                    st.error(f"❌ Server error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"🚨 Request failed: {e}")
    else:
        st.warning("⚠️ Please upload both a video and an image.")