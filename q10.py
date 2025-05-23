# -*- coding: utf-8 -*-
"""q10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18RUJ-gyyU6TTFmLPLKFD79WmSyBtllw0
"""

OK_FORMAT = False
name = "q10"



def split_dataframes(df):
    """
    Splits the dataframe into two separate dataframes based on the `category` column.

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        tuple: A tuple of two dataframes: (cereals_df, pulses_df).
    """
    df = df.copy()  # Avoid modifying the original dataframe

    cereals_df = df[df["category"].str.lower() == "cereals and tubers"].reset_index(drop=True)
    pulses_df = df[df["category"].str.lower() == "pulses and nuts"].reset_index(drop=True)

    return cereals_df, pulses_df