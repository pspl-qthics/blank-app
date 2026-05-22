import pandas as pd
import os
import json

TABLE_FOLDER = "data/tables"

os.makedirs(TABLE_FOLDER, exist_ok=True)

def get_table_path(table_name):

    return f"{TABLE_FOLDER}/{table_name}.csv"

def get_meta_path(table_name):

    return f"{TABLE_FOLDER}/{table_name}_meta.json"

def save_table(df, table_name):

    path = get_table_path(table_name)

    df.to_csv(path, index=False)

def save_column_config(

    column_config,

    table_name
):

    path = get_meta_path(table_name)

    with open(path, "w") as f:

        json.dump(
            column_config,
            f,
            indent=4
        )

def load_table(table_name):

    path = get_table_path(table_name)

    if os.path.exists(path):

        try:

            return pd.read_csv(path)

        except pd.errors.EmptyDataError:

            return pd.DataFrame()

    return pd.DataFrame()

def load_column_config(table_name):

    path = get_meta_path(table_name)

    if os.path.exists(path):

        with open(path, "r") as f:

            return json.load(f)

    return {}

def list_tables():

    files = os.listdir(TABLE_FOLDER)

    return [

        f.replace(".csv", "")

        for f in files

        if f.endswith(".csv")
    ]