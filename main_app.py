import streamlit as st
from PIL import Image

st.title("Hello, Streamlit!")
st.caption("This is a simple Streamlit app.")


st.subheader("自己紹介")
st.text("私はChatGPT、OpenAIが開発したAI言語モデルです。")

# 画像
image = Image.open("./data/01.jpg")
st.image(image,width=300)
