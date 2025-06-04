
import streamlit as st
import requests

st.set_page_config(page_title="Face Swap Cloud", page_icon="🎥")

st.title("🎥 Face Swap Cloud")
st.markdown("Upload a video and a face image to apply face swap.")

video_file = st.file_uploader("Upload Video File (mp4, mov)", type=["mp4", "mov", "mpeg4"])
image_file = st.file_uploader("Upload Face Image (jpg, png)", type=["jpg", "jpeg", "png"])
resolution = st.selectbox("Output Resolution", options=["720", "1080"], index=0)

if st.button("Launch FaceSwap"):
    if not video_file or not image_file:
        st.error("Please upload both a video and a face image.")
    else:
        with st.spinner("Swapping faces..."):
            files = {
                "source": ("video.mp4", video_file.read(), "video/mp4"),
                "target": ("image.jpg", image_file.read(), "image/jpeg"),
            }
            data = {"resolution": resolution}
            try:
                response = requests.post(
                    url=st.secrets["BACKEND_URL"],
                    files=files,
                    data=data
                )
                if response.status_code == 200:
                    st.success("✅ Face swap completed!")
                    st.video(response.content)
                else:
                    st.error(f"❌ Server error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Connection failed: {e}")
