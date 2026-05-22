import pandas as pd

def create_default_dataframe():

    return pd.DataFrame({

        "_select": []
    })

def create_default_column_config():

    return {

        "_select": {

            "type": "system"
        }
    }