import streamlit as st

from components.column_manager import (
    add_column_popup
)

from components.row_manager import (
    add_rows_popup
)

from components.table_manager import (
    render_table_manager
)

from engine.storage import (

    save_table,

    save_column_config
)


def render_sidebar():

    st.sidebar.header("Controls")

    # Add column popup
    add_column_popup()

    # Add rows popup
    add_rows_popup()

    render_table_manager()

    st.sidebar.divider()

    # DELETE SELECTED ROWS
    if st.sidebar.button(
        "Delete Selected Rows"
    ):

        df = st.session_state.df

        df = df[
            df["_select"] == False
        ]

        df = df.reset_index(
            drop=True
        )

        st.session_state.df = df

        save_table(

            df,

            st.session_state.current_table
        )

        st.rerun()

    st.sidebar.divider()

    # COLUMN LIST
    st.sidebar.subheader("Columns")


    for column, config in st.session_state.column_config.items():

        if column.startswith("_"):
            continue

        st.sidebar.write(

            f"{column} ({config['type']})"
        )

        rename_columns = [

    col

    for col in st.session_state.df.columns

    if not col.startswith("_")
]

    if rename_columns:

        rename_old = st.sidebar.selectbox(

            "Rename Column",

            rename_columns
        )

        rename_new = st.sidebar.text_input(

            "New Column Name"
        )

        if st.sidebar.button("Rename Column"):

            st.session_state.df = (

                st.session_state.df.rename(

                    columns={
                        rename_old: rename_new
                    }
                )
            )

            if rename_old in st.session_state.column_config:

                st.session_state.column_config[
                    rename_new
                ] = (

                    st.session_state.column_config.pop(
                        rename_old
                    )
                )

            save_table(

                st.session_state.df,

                st.session_state.current_table
            )

            save_column_config(

                st.session_state.column_config,

                st.session_state.current_table
            )

            st.rerun()

    st.sidebar.divider()

    # DELETE COLUMN
    st.sidebar.subheader(
        "Delete Column"
    )

    columns = [

        col

        for col in st.session_state.df.columns

        if not col.startswith("_")
    ]

    if columns:

        column_to_delete = st.sidebar.selectbox(

            "Select Column",

            columns
        )

        if st.sidebar.button(
            "Delete Column"
        ):

            st.session_state.df = (
                st.session_state.df.drop(

                    columns=[column_to_delete]
                )
            )

            if column_to_delete in st.session_state.column_config:

                del st.session_state.column_config[
                    column_to_delete
                ]

            save_table(
                st.session_state.df
            )

            st.rerun()