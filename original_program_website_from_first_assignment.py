import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=":beaming_face_with_smiling_eyes:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/208d8c64-760f-4194-9330-b865f0b8e4f5/pPgWIHeYbr.json")
lottie_image = load_lottieurl("https://lottie.host/547a3f8f-84bb-4324-9f19-fb1518d9b9ca/eRnHTDoqjz.json")

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hi! Welcome to my page.")
        st.title("This is Chloe at your service")
        st.write("You want to know how did I make this page?")
        st.write("[Learn More. >](https://github.com/mrychlnn)")
    with right_column:
        st_lottie(lottie_image, height=300, key="image")

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
            - I'm a Computer Engineering student at Polytechnic University of the Philippines - Santa Mesa
            - I'm passionate about learning more about programming and other fields, especially hardware and software.

            If your interested on learning more about me then kindly visit my Facebook Account.
            """
        )
        st.write("[Facebook Account >](https://www.facebook.com/share/1B9f68pVRD/)")
    
    with right_column:
        st_lottie(lottie_coding, height=270, key="coding")

with st.container():
    st.write("---")
    st.subheader("Connect with me")
    st.write("#####")
    st.write("Email Account: lunamarychloeanne@gamil.com")
    st.write("GitHub Account: [mrychlnn](https://github.com/mrychlnn)")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)
    