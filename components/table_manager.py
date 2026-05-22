import streamlit as st
import pandas as pd
import os
import shutil

from engine.storage import (
    list_tables,
    load_table,
    save_table
)

def render_table_manager():

    st.sidebar.subheader("Tables")

    rename_table = st.sidebar.text_input(
        "Rename Current Table",

        key="rename_table_input"
    )

    if st.sidebar.button("Rename Table"):

        old_csv = (
            f"data/tables/"
            f"{st.session_state.current_table}.csv"
        )

        new_csv = (
            f"data/tables/"
            f"{rename_table}.csv"
        )

        old_meta = (
            f"data/tables/"
            f"{st.session_state.current_table}_meta.json"
        )

        new_meta = (
            f"data/tables/"
            f"{rename_table}_meta.json"
        )

        if os.path.exists(old_csv):

            shutil.move(
                old_csv,
                new_csv
            )

        if os.path.exists(old_meta):

            shutil.move(
                old_meta,
                new_meta
            )

        st.session_state.current_table = (
            rename_table
        )

    st.rerun()

    if st.sidebar.button("Load Table"):

        st.session_state.df = load_table(
            selected_table
        )

        st.session_state.current_table = (
            selected_table
        )

        st.rerun()
    
    if st.sidebar.button("Delete Table"):

        table_path = f"data/tables/{selected_table}.csv"

        if os.path.exists(table_path):

            os.remove(table_path)

        st.session_state.current_table = "untitled"

        st.session_state.df = pd.DataFrame({

            "_select": []
        })

        st.rerun()

    csv_data = st.session_state.df.to_csv(

        index=False
        )
    st.sidebar.download_button(

        "Download CSV",

        csv_data,

        file_name=f"{st.session_state.current_table}.csv",

        mime="text/csv"
    )

    new_table = st.sidebar.text_input(
        "New Table Name"
    )

    if st.sidebar.button("Create Table"):

        st.session_state.current_table = (
            new_table
        )

        st.session_state.df = pd.DataFrame({

            "_select": []
        })

        save_table(

            st.session_state.df,

            new_table
        )

        st.rerun()
    