import streamlit as st
from PIL import Image
from streamlit_extras.colored_header import colored_header

logo = Image.open("logo.png")
if "input_parqet_file" not in st.session_state:
    st.session_state["input_parqet_file"]=None

if "myfile" not in st.session_state:
    st.session_state.myfile=None

st.set_page_config(page_title="View Demo",layout="centered",page_icon=logo)
colored_header(label="View Demo",description="Learn how to use ParquetSage",color_name="violet-70")
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
