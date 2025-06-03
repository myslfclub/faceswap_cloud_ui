
import streamlit as st
import requests

st.set_page_config(page_title="Face Swap Cloud", layout="centered")

st.title("🎥 Face Swap Cloud")
st.markdown("Upload a video and a face image to apply face swap.")

video_file = st.file_uploader("Upload Video File (mp4, mov)", type=["mp4", "mov", "mpeg4"])
image_file = st.file_uploader("Upload Face Image (jpg, png)", type=["jpg", "jpeg", "png"])
resolution = st.selectbox("Output Resolution", ["720", "1080", "4k"])

if st.button("Launch FaceSwap"):
    if video_file and image_file:
        with st.spinner("Sending files to backend..."):
            files = {
                "video": (video_file.name, video_file, video_file.type),
                "image": (image_file.name, image_file, image_file.type),
            }
            data = {"resolution": resolution}
            try:
                response = requests.post(
                    url=st.secrets["BACKEND_URL"],
                    files=files,
                    data=data,
                    timeout=180,
                )
                if response.status_code == 200:
                    output_path = "output.mp4"
                    with open(output_path, "wb") as f:
                        f.write(response.content)
                    st.success("✅ Face swap completed.")
                    st.video(output_path)
                else:
                    st.error(f"❌ Server error: {response.status_code}\n{response.text}")
            except Exception as e:
                st.error(f"❌ Connection failed: {e}")
    else:
        st.warning("Please upload both a video and a face image.")
