
import streamlit as st
import requests

st.set_page_config(page_title="Face Swap Cloud", layout="centered")
st.title("🎭 Face Swap Cloud")
st.write("Upload a video and a face image to apply face swap.")

video_file = st.file_uploader("Upload Video File (mp4, mov)", type=["mp4", "mov", "mpeg4"])
face_image = st.file_uploader("Upload Face Image (jpg, png)", type=["jpg", "jpeg", "png"])
resolution = st.selectbox("Output Resolution", options=["480", "720", "1080"])

if st.button("Launch FaceSwap"):
    if not video_file or not face_image:
        st.error("Please upload both a video and a face image.")
    else:
        files = {
            "video": (video_file.name, video_file.read(), video_file.type),
            "face": (face_image.name, face_image.read(), face_image.type)
        }
        data = {"resolution": resolution}
        headers = {"X-API-Key": st.secrets["API_KEY"]}
        try:
            response = requests.post(
                st.secrets["BACKEND_URL"],
                files=files,
                data=data,
                headers=headers
            )
            if response.status_code == 200:
                with open("result.mp4", "wb") as f:
                    f.write(response.content)
                st.success("✅ Face swap completed!")
                st.video("result.mp4")
            else:
                st.error(f"❌ Server error: {response.status_code} {response.text}")
        except Exception as e:
            st.error(f"❌ Error: {e}")
