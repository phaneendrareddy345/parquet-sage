import streamlit as st
from streamlit_extras.colored_header import colored_header
import requests
from streamlit_lottie import st_lottie
from PIL import Image

logo = Image.open("logo.png")

if "input_parqet_file" not in st.session_state:
    st.session_state["input_parqet_file"]=None

if "myfile" not in st.session_state:
    st.session_state.myfile=None
st.set_page_config(layout="wide",page_title="Contact Us",page_icon=logo)
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)
st.markdown("""
  <style>
    .st-emotion-cache-lrlib eczjsme9 {
      margin-top: -75px;
    }
  </style>
""", unsafe_allow_html=True)
colored_header(label="Contact Us",description="We'd love to hear from you!",color_name="violet-70")
## contact form
with open("form.html","r") as frm:
    frm_css = frm.read()
form="""<form action="https://formsubmit.co/ittechtech5555@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your Message"></textarea>
     <button type="submit">Send</button>
</form>"""
form_c,animation = st.columns(2)
#form_c.markdown(f"""<style>{form_c}</style>""",unsafe_allow_html=True)
# form_c.markdown("""## Contact Us""")
# form_c.caption("We'd love to hear from you!")
form_c.markdown(frm_css,unsafe_allow_html=True)
#form_c.markdown()
#animation.lottie("Animation")
def load_lottie():
    lottie_file = requests.get("https://lottie.host/63193370-2bf7-423c-9f4e-9ec9e0170741/PHSTSBfTG9.json")
    if lottie_file.status_code!=200:
        return None
    return lottie_file.json()

lottie = load_lottie()
with animation:
    st_lottie(lottie,key="contactus")