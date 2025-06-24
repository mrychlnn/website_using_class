import streamlit as st
from website_oop_version.base_page import BaseWebPage
from website_oop_version.lottie_loader import load_lottieurl
from website_oop_version.header_for_website import header_section
from website_oop_version.about_me import about_me_section
from website_oop_version.contact_me import connect_section
from website_oop_version.style import local_css
from website_oop_version.snowflakes import snowflake_effect

class ChloeWebsite(BaseWebPage):
    def __init__(self):
        super().__init__()
        self.lottie_coding = load_lottieurl("https://lottie.host/208d8c64-760f-4194-9330-b865f0b8e4f5/pPgWIHeYbr.json")
        self.lottie_image = load_lottieurl("https://lottie.host/547a3f8f-84bb-4324-9f19-fb1518d9b9ca/eRnHTDoqjz.json")
        st.set_page_config(page_title="My Webpage", page_icon=":beaming_face_with_smiling_eyes:", layout="wide")

    def run(self):
        header_section(self.lottie_image)
        about_me_section(self.lottie_coding)
        connect_section()
        local_css("style/style.css")
        snowflake_effect()