import streamlit as st
import pandas as pd
import hashlib

from engine.storage import (
    save_table,
    load_table
)

def get_df_hash(df):

    return hashlib.md5(

        df.to_json().encode()

    ).hexdigest()

def render_table():

    if "df" not in st.session_state:

        st.session_state.df = load_table()
    
    if "_select" not in st.session_state.df.columns:

        st.session_state.df.insert(
            0,
            "_select",
            False
        )

    st.session_state.df = (
        st.session_state.df.astype(str)
    )

    for col in st.session_state.df.columns:

        if col == "_select":
            continue

        column_type = (
            st.session_state
            .column_config
            .get(col, {})
            .get("type", "text")
        )

        if column_type == "number":

            st.session_state.df[col] = pd.to_numeric(

                st.session_state.df[col],

                errors="coerce"
            )

        else:

            st.session_state.df[col] = (

                st.session_state.df[col]
                .astype(str)
            )

    edited_df = st.data_editor(

        st.session_state.df,

        use_container_width=True,

        num_rows="dynamic",

        key="main_table",

        column_config={

            "_select": st.column_config.CheckboxColumn(
                "Select"
            )
        }
    )


    current_hash = get_df_hash(
    edited_df
    )

    if current_hash != st.session_state.last_save_hash:

        st.session_state.df = edited_df

        save_table(

            edited_df,

            st.session_state.current_table
        )

        st.session_state.last_save_hash = current_hash

    st.session_state.df = edited_df

