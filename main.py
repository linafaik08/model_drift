import pandas as pd

def get_table_stats(df):
    """Return main statistics of a dataframe df"""
    table = df.describe()
    return table
