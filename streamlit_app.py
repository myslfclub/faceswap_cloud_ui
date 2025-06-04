import streamlit as st
import requests

st.set_page_config(page_title="Face Swap Cloud", page_icon="🎭", layout="centered")
st.title("🎭 Face Swap Cloud")
st.markdown("Upload a video and a face image to apply face swap.")

video_file = st.file_uploader("Upload Video File (mp4, mov)", type=["mp4", "mov", "mpeg4"])
face_file = st.file_uploader("Upload Face Image (jpg, png)", type=["jpg", "jpeg", "png"])
resolution = st.selectbox("Output Resolution", ["480", "720", "1080"])

if st.button("Launch FaceSwap"):
    if not video_file or not face_file:
        st.error("Please upload both a video and a face image.")
    else:
        with st.spinner("Swapping faces..."):
            files = {
                "video": (video_file.name, video_file, video_file.type),
                "face": (face_file.name, face_file, face_file.type)
            }
            data = {"resolution": resolution}
            try:
                backend_url = st.secrets["BACKEND_URL"]
                response = requests.post(backend_url, files=files, data=data)
                if response.status_code == 200:
                    st.success("✅ Face swap completed!")
                    st.video(response.content)
                else:
                    st.error(f"❌ Server error: {response.status_code} {response.text}")
            except Exception as e:
                st.error(f"Exception: {e}")