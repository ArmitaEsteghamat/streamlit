from PIL import Image
import streamlit as st
st.title('آپلود تصویر')


img_file = st.file_uploader('pls choice an image...',type=['jpg','jpeg','png'])

if img_file is not None:
    image = Image.open(img_file)
    st.image(image,caption='uploaded image...',use_container_width=True)


