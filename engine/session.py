import streamlit as st
import pandas as pd

from engine.storage import (

    load_table,

    load_column_config
)

def initialize_session():

    if "current_table" not in st.session_state:

        st.session_state.current_table = "untitled"

    if "df" not in st.session_state:

        st.session_state.df = load_table(
            st.session_state.current_table
        )

    if "show_column_popup" not in st.session_state:

        st.session_state.show_column_popup = False

    if "show_row_popup" not in st.session_state:

        st.session_state.show_row_popup = False

    if "column_config" not in st.session_state:

        st.session_state.column_config = (

            load_column_config(

                st.session_state.current_table
            )
        )

    if "last_save_hash" not in st.session_state:

        st.session_state.last_save_hash = ""
