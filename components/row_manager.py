import streamlit as st
import pandas as pd

from engine.storage import save_table

def add_rows_popup():

    if "df" not in st.session_state:
        return

    if st.sidebar.button("Add Rows"):

        st.session_state.show_row_popup = True

    if st.session_state.get("show_row_popup"):

        with st.sidebar.form("row_form"):

            row_count = st.number_input(

                "Number of Rows",

                min_value=1,

                value=10
            )

            submit = st.form_submit_button(
                "Add"
            )

            if submit:

                empty_rows = pd.DataFrame(

                    "",

                    index=range(row_count),

                    columns=st.session_state.df.columns
                )

                st.session_state.df = pd.concat(

                    [
                        st.session_state.df,
                        empty_rows
                    ],

                    ignore_index=True
                )

                save_table(
                    st.session_state.df,

                    st.session_state.current_table
                )

                st.session_state.show_row_popup = False

                st.rerun()