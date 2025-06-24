import streamlit as st

def snowflake_effect():
    animation_symbol = "❄"
    st.markdown(
        "".join(
            f'<div class="snowflake">{animation_symbol}</div>\n'
            for snow in range(20)
        ),
        unsafe_allow_html=True,
    )