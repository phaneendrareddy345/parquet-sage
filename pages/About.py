import streamlit as st
import pandas as pd
import plotly.express as px
import duckdb
from datetime import datetime,date
from streamlit_extras.grid import grid
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.colored_header import colored_header
from streamlit_ace import st_ace
from PIL import Image

logo = Image.open("logo.png")

if "input_parqet_file" not in st.session_state:
    st.session_state["input_parqet_file"]=None

if "myfile" not in st.session_state:
    st.session_state.myfile=None
st.set_page_config(layout="wide",page_title="About",page_icon=logo)
st.markdown("""
        <style>
               .block-container {
                    padding-top: 2rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)
# st.markdown("""
#   <style>
#     .st-emotion-cache-lrlib eczjsme9 {
#       margin-top: -75px;
#     }
#   </style>
# """, unsafe_allow_html=True)
colored_header(label="About",description="Get to know more about ParquetSage",color_name="violet-70")
#st.markdown("## About")
with open("readme.md","r") as about_md:
    about = about_md.read()

st.markdown(about)
footer_f = """<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    color: #232452;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
}
.ftr:link, .ftr:visited {
    color: #7743DB;
    background-color: transparent;
    text-decoration: underline;
}
.ftr:hover, .ftr:active {
    background-color: transparent;
    text-decoration: underline;
}
</style>

<div class="footer">
    <p>Created with ❤ by <a class="ftr" href="https://www.linkedin.com/in/j-v-phanindra-reddy" target="_blank">Phani</a></p>
</div>
"""

st.markdown(footer_f,unsafe_allow_html=True)
