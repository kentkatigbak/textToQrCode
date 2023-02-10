# Libraries
import qrcode
import streamlit as st
from PIL import Image
import io

# Page configurations

st.set_page_config(page_title="Text to QR Code", layout="centered", initial_sidebar_state="collapsed")

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)


# Application
st.title('QR Code Generator from Text')

col1, col2 = st.columns([1,1])

with col1:
    st.subheader("Enter your message here")
    title = st.text_area(label='', value='', label_visibility="hidden")
    generate_button = st.button("Generate")

with col2:
    def load_data(message):
        qr = qrcode.QRCode()
        qr.add_data(message)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        return img
    img = load_data(title)

    buf = io.BytesIO()
    img.save(buf)
    byte_im = buf.getvalue()
    st.image(byte_im, caption='Generated QR Code')

st.write("________________________________")
st.write("Created by Kent Katigbak | Follow me on tiktok - [@kentjk.ie](https://www.tiktok.com/@kentjk.ie?_t=8ZlD8kgkgUc&_r=1)")