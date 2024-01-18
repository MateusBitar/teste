import streamlit as st
import base64


def image_to_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    
    
img = image_to_base64("tenis.jpg")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("data:image/png;base64,{img}");
background-size: cover;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html= True)
st.title("Teste")
