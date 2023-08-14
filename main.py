import streamlit as st
import os
from dotenv import load_dotenv
from src.img2txt import img2txt
from src.txt2story import txt2story
from src.txt2speech import txt2speech

def upload_image(image) -> str:
    safe_name = image.name.replace(" ", "_").lower()

    upload_folder = os.getenv('UPLOAD_FOLDER')
    if not upload_folder:
        raise ValueError("UPLOAD_FOLDER environment variable is not set!")

    file_path = os.path.join(upload_folder, safe_name)
    os.makedirs(upload_folder, exist_ok=True)

    with open(file_path, "wb") as fp:
        fp.write(image.getbuffer())

    return file_path

def main():
    load_dotenv()
    st.sidebar.title("Image Story Teller")
    st.sidebar.markdown("A simple app to generate a story from an image")
    st.sidebar.markdown("Built with Streamlit and Huggingface")
    st.sidebar.markdown("By [Imad Nami](https://twitter.com/najmi_imad)")
    st.sidebar.markdown("Source code: [Github](https://github.com/najmi9/image-2-story)")
    st.sidebar.header("Used Models: ")
    st.sidebar.markdown("Image to text: [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base)")
    st.sidebar.markdown("Text to story: [Google PALM API](https://makersuite.google.com/)")
    st.sidebar.markdown("Text to speech: [espnet/kan-bayashi_ljspeech_vits](https://huggingface.co/espnet/kan-bayashi_ljspeech_vits)")

    st.title("Image Story Teller")
    image_uploaded = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    # check if the image is uploaded
    if image_uploaded is not None:
        file_path = upload_image(image_uploaded)
        st.image(image_uploaded, caption="Uploaded Image", use_column_width=True)
        st.write("")
        st.header("Generating story...")

        with st.spinner("Generating story..."):
            text = img2txt(file_path)
            story = txt2story(text)
            filepath = txt2speech(story)
            st.audio(filepath)
            st.write(story)

if __name__ == "__main__":
    main()
