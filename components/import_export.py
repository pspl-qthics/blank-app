import streamlit as st
import pandas as pd

def render_import_export():

    uploaded_file = st.sidebar.file_uploader(

        "Upload CSV or Excel",

        type=["csv", "xlsx"]
    )

    if uploaded_file:

        if uploaded_file.name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)

        else:

            df = pd.read_excel(uploaded_file)

        st.session_state.df = df

        st.rerun()

csv = st.session_state.df.to_csv(
    index=False
)

st.sidebar.download_button(

    "Download CSV",

    csv,

    file_name="table.csv",

    mime="text/csv"
)