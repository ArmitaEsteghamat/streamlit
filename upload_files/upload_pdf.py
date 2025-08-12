import streamlit as st
import base64

st.title("PDF Upload")

pdf_file = st.file_uploader("Upload your PDF file", type=['pdf'])

if pdf_file is not None:
    base64_pdf = base64.b64encode(pdf_file.read()).decode("utf-8")

    pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>
    """

    st.markdown(pdf_display, unsafe_allow_html=True)
