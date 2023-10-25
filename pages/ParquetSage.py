import streamlit as st
import pandas as pd
import plotly.express as px
import duckdb
from datetime import datetime,date
from streamlit_extras.grid import grid
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.colored_header import colored_header
from streamlit_ace import st_ace
import io
import openpyxl
from PIL import Image

logo = Image.open("logo.png")

if "input_parqet_file" not in st.session_state:
    st.session_state["input_parqet_file"]=None

if "myfile" not in st.session_state:
    st.session_state.myfile=None
st.set_page_config(layout="wide",page_title="Parquet Sage",page_icon=logo)
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
# st.markdown("""
#   <style>
#     .st-emotion-cache-lrlib eczjsme9 {
#       margin-top: -75px;
#     }
#   </style>
# """, unsafe_allow_html=True)
colored_header(label="Parquet Sage",description="Seamlessly Preview and Query your Parquet Files",color_name="violet-70")
st.caption("⚠️ We dont store your data")
with st.expander("Browse Files"):
    input_parqet_file = st.file_uploader("Upload a Parquet File",type="PARQUET")
prev_data,slq_editor = st.tabs(["Preview File","SQL Editor"])
with prev_data:
    st.caption("Preview data from parquet file using UI")
    @st.cache_data
    def read_data():
        st.session_state.input_parqet_file=input_parqet_file
        myfile=pd.read_parquet(io.BytesIO(st.session_state["input_parqet_file"].getvalue()))
        st.session_state.myfile=myfile
        return myfile
    def load_dataframe_ui():
        myfile = read_data()
        df_ui = dataframe_explorer(myfile,case=True)
        df_ui_grid = grid([1,1])
        df_ui_grid.info("Displaying only top 1000 rows")
        df_ui_grid.info(f"Total Number of Records {len(myfile)}")
        st.dataframe(df_ui)
    # limit_rows = st.checkbox("limit rows")
    # if limit_rows:
    #     limit = st.number_input("Number of Rows",value=1000,min_value=1,max_value=10000)
    # else:
    #     limit=None

    if input_parqet_file is not None:
        load_dataframe_ui()

with slq_editor:
    st.caption("Get more insights from parquet file using SQL Editor")
    query_engine,results = st.columns([3,1])
    #myfile = pd.read_excel("/app/sample_data.xlsx",index_col=None)
    myfile = st.session_state.myfile
    #enu = st.sidebar.selectbox("Menu",("Explore Data","SQL Editor"))
    def query_engine_fn(query):
        st_time = datetime.now()
        res=duckdb.query(query).to_df()
        ed_time = datetime.now()
        time_taken = (ed_time-st_time).total_seconds()
        return res,time_taken
    
    def save_as_excel():
        output = io.BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        res.to_excel(writer, index=False, sheet_name='results')
        writer.save()
        data = output.getvalue()
        return data



    with query_engine:
        st.markdown("### SQL Editor")
        st.caption("Run your sql queries")
        query=st_ace(language="sql",keybinding="vscode",placeholder="/* use myfile as tablename. example: select count(*) from myfile*/")

        #query=st.text_area(label="Query",help="SELECT [COLS] FORM myfile",placeholder="""/*use myfile as tablename
        #select * from myfile*/""")
    #     #m = st.markdown("""
    # <style>
    # div.stButton > button:first-child {
    #     background-color: #7743DB;
    #     color: #FFFFFF;
    # }
    # div.stButton > button:active { color: #7743DB;
    #     background-color: #FFFFFF;}
    # div.stButton > button:hover {border-color: #3B216D}
    # </style>""", unsafe_allow_html=True)
        #run_query = st.button("▶️ Run")
        if query:
            try:
                res,time_taken=query_engine_fn(query)
                #st.title("Results")
                #res_grid = grid([3,3,3])
                st.success("Query Executed Successfully!")
                res_tab,exe_tab=st.tabs(["Results","Execution Details"])
                #exe_tab.info(f"Query took {time_taken} seconds to Finish")
                #exe_tab.info(f"Query returned {len(res)} rows")
                exe_tab.markdown(f"**Execution time (Seconds)**: `{time_taken}`")
                exe_tab.markdown(f"**Records returned**: `{len(res)}`")
                res_tab.dataframe(res)
                excel=save_as_excel()
                # file_name = "ps_results"+datetime.now().strftime("%Y_%m_%d_%H_%M_%S")+".xlsx"
                # st.download_button("Save Results",data=res,mime="application/octet-stream",file_name=file_name)
            except Exception as e:
                st.title("Results")
                st.error(f"Query Execution Failed with error: {e}")
            st.download_button(label='📥 Save Result',
                                data=excel,
                                file_name= 'pg_results.xlsx',
                                mime="application/vnd.ms-excel")
