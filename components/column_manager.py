import streamlit as st

from engine.storage import (

    save_table,

    save_column_config
)

def add_column_popup():

    if "df" not in st.session_state:
        return

    if st.sidebar.button("Add Column"):

        st.session_state.show_column_popup = True

    if st.session_state.get("show_column_popup"):

        with st.sidebar.form("column_form"):

            column_name = st.text_input(
                "Column Name"
            )

            column_type = st.selectbox(

                "Column Type",

                [
                    "text",
                    "ai",
                    "url",
                    "number"
                ]
            )

            submit = st.form_submit_button(
                "Create Column"
            )

            if submit:

                 if column_name:

                    st.session_state.df[column_name] = ""

                    st.session_state.column_config[
                        column_name
                    ] = {

                        "type": column_type
                    }

                    save_table(
                        st.session_state.df,

                        st.session_state.current_table
                    )
                    save_column_config(

                        st.session_state.column_config,

                        st.session_state.current_table
                    )

                    st.session_state.show_column_popup = False

                    st.rerun()