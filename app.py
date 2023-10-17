import streamlit as st
import pandas as pd
import plotly.express as px
import duckdb
st.set_page_config(layout="wide")
query_engine,results = st.columns([3,1])
myfile = pd.read_excel("/app/sample_data.xlsx",index_col=None)
with query_engine:
    st.title("SQL Editor")
    st.caption("Run your sql queries")

    query=st.text_area(label="query",help="SELECT [COLS] FORM myfile")
    run_query = st.button("Run")
    if run_query:
        try:
            res=duckdb.query(query).to_df()
            st.title("Results")
            st.success("Query Executed Successfully!")
            st.dataframe(res)
        except Exception as e:
            st.title("Results")
            st.error(f"Query Execution Failed with error: {e}")

with results:
    st.title("Query Details")
    st.subheader(f"Records Returned: {len(res)}")
        






