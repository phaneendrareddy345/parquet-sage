import streamlit as st
import pandas as pd
import plotly.express as px
import duckdb
from datetime import datetime,date
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header
from streamlit_extras.dataframe_explorer import dataframe_explorer
import io
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container
from PIL import Image
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_lottie import st_lottie
from streamlit_extras.streaming_write import write
import time
from st_pages import Page,show_pages

logo = Image.open("logo.png")
st.set_page_config(layout="wide",page_title="Home",page_icon=logo)
show_pages(
    [
        Page("streamlit_app.py","Home"),
        Page("pages/ParquetSage.py","ParquetSage"),
        Page("pages/View Demo.py","View Demo"),
        Page("pages/Contact Us.py","Contact Us"),
        Page("pages/About.py","About")
    ]
)
# st.markdown("""<h1 style='text-align:center'>Parquet Sage</h1>""",unsafe_allow_html=True)
with open("line.html","r") as line:
    line_f = line.read()

def load_lottie():
    import requests
    lottie = requests.get("https://lottie.host/39048ada-be57-4b44-8fb1-1f0fd16671df/uWXQc7EQQF.json")
    if lottie.status_code!=200:
        return None
    return lottie.json()

lotti_animation = load_lottie()

def stream_tag_line():
    tagline="Seamlessly Preview and Query your Parquet Files"
    for word in tagline.split():
        yield word+" "
        time.sleep(0.1)

#st.markdown("""<style>footer{visibility: hidden;}header {visibility: hidden;}</style>""",unsafe_allow_html=True)

#st.markdown(line_f,unsafe_allow_html=True)
#add_vertical_space(5)
with open("button.css","r") as button:
    button_css = button.read()
m = st.markdown(f"<style>{button_css}</style>",unsafe_allow_html=True)
home_cnt=st.container()
with home_cnt:
    content,animation = st.columns((1,1))
    with content:
        add_vertical_space(5)
    content.markdown("""<h1 style='text-align:center'>Parquet Sage</h1>""",unsafe_allow_html=True)
    content.markdown(line_f,unsafe_allow_html=True)
    content.markdown("""<h4 style='text-align:center'>Seamlessly Preview and Query your Parquet Files</h4>""",unsafe_allow_html=True)
    #write(stream_tag_line)
    #                box-shadow: 0 8px 16px 0 rgba(119, 67, 219, 0.5);
    get_started = content.button("Get Started 🡲")
    with animation:
        with stylable_container(key="img",css_styles="""
            div[data-testid="stImage"] > img{
                border-radius: 10px;
                box-shadow: 0 8px 16px 0 rgba(119, 67, 219, 0.5);
            }
        """):
            st.image("bg.png",use_column_width=True)



with open("cards.html",mode="r") as cards:
    card_f = cards.read()
# with home_cnt:
#     home_cnt.markdown("""<h4 style='text-align:center'>Seamlessly Preview and Query your Parquet Files</h4>""",unsafe_allow_html=True)
#     preview,sql_editor,visualize,data_quality = st.columns(4)
#     preview.markdown(card_f.replace("CardName","Preview File"),unsafe_allow_html=True)
#     sql_editor.markdown(card_f.replace("CardName","SQL Editor"),unsafe_allow_html=True)
#     visualize.markdown(card_f.replace("CardName","Visualize"),unsafe_allow_html=True)
#     data_quality.markdown(card_f.replace("CardName","Data Quality Checks"),unsafe_allow_html=True)

##footer
# with open("footer.html","r") as footer:
#    footer_f = footer.read()
#   background-color: white;
footer_f = """<style>
.footer {
    left: 0;
    bottom: 0;
    position: fixed;
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

if get_started:
    switch_page("ParquetSage")

