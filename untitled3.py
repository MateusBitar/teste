import streamlit as st
import base64

@st.cache_data
def img_to_base64(foto):
    with open(foto, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = img_to_base64("tenis.jpg")

page = f"""
<style>
[data-testid="stAppViewContainer"] > div:first-child{{
background-image: url("data:image/jpg;base64,{img}");
    }}

</style>
"""
st.markdown(page, unsafe_allow_html = True) 
