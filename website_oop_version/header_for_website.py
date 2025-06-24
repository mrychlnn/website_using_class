import streamlit as st
from streamlit_lottie import st_lottie

def header_section(lottie_image):
    with st.container():
        left_column, right_column =  st.columns(2)
        with left_column:
            st.subheader("Hi! Welcome to my page.")
            st.title("This is Chloe at your service")
            st.write("You want to know how did I make this page?")
            st.write("[Learn More.>](https://github.com/mrychlnn)")
        with right_column:
            st_lottie(lottie_image, height=300, key="image")