import streamlit as st

code = '''
import streamlit as st
st.title("Hello, Streamlit!")
python
'''
st.code(code, language='python')