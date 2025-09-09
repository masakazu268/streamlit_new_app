import streamlit as st
from PIL import Image

st.title("Hello, Streamlit!")
st.caption("This is a simple Streamlit app.")


st.subheader("自己紹介")
st.text("私は、まさかず。python独学中の60歳代です。")

# 画git add .像
image = Image.open("./data/01.jpg")
st.image(image,width=300)
