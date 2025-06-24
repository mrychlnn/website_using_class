import streamlit as st
from streamlit_lottie import st_lottie

def about_me_section(lottie_coding):
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Things about me:")
            st.write("#####")
            st.write(
                """
                - My name is Mary Chloe Anne A. Luna
                - 18 years old
                - I'm a Computer Engineering student at Polytechnic University of the Philippines - Sta. Mesa
                - I'm passionate about learning more about programming and other fields, especially hardware and software.

                If you're interested in learning more about me then kindly visit my Facebook Account.

"""
            )
            st.write("[Facebook Account>](https://www.facebook.com/share/1B9f68pVRD/)")
        with right_column:
            st_lottie(lottie_coding, height=270, key="coding")