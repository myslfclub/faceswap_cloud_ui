import streamlit as st
import requests
import base64

st.set_page_config(page_title="Face Swap Cloud", layout="centered")

st.title("🎥 Face Swap Cloud")
st.markdown("Upload a video and a face image to apply face swap.")

video_file = st.file_uploader("Upload Video File (mp4, mov)", type=["mp4", "mov"])
image_file = st.file_uploader("Upload Face Image (jpg, png)", type=["jpg", "jpeg", "png"])
output_resolution = st.selectbox("Output Resolution", options=["720", "480", "360"], index=0)

if st.button("Launch FaceSwap") and video_file and image_file:
    with st.spinner("Swapping faces..."):
        files = {
            "video": (video_file.name, video_file, "video/mp4"),
            "face": (image_file.name, image_file, "image/jpeg"),
        }
        data = {"resolution": output_resolution}
        try:
            response = requests.post(
                "https://faceswap-cloud-backend-1.onrender.com/faceswap",
                files=files,
                data=data,
                timeout=300
            )
            if response.status_code == 200:
                st.success("✅ Face swap completed!")
                video_bytes = response.content
                b64 = base64.b64encode(video_bytes).decode()
                video_html = f'''
                    <video width="100%" height="auto" controls>
                        <source src="data:video/mp4;base64,{b64}" type="video/mp4">
                        Your browser does not support the video tag.
                    </video>
                '''
                st.markdown(video_html, unsafe_allow_html=True)
            else:
                st.error(f"❌ Server error: {response.status_code} {response.text}")
        except Exception as e:
            st.error(f"❌ Request failed: {e}")
