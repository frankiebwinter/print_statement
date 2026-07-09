import streamlit as st

st.write("Hello, world!")
 
name = st.text_input("What's your name?")
 
if name:
    st.write(f"Hello, {name}!")
 
