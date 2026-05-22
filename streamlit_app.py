import streamlit as st

from engine.session import initialize_session

from components.sidebar import render_sidebar
from components.table import render_table

st.set_page_config(layout="wide")

initialize_session()

st.title("AI Spreadsheet")

render_sidebar()

render_table()