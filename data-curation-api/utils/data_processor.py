import pandas as pd

def clean_data(df):
    """Basic data cleaning: remove duplicates, fill missing values."""
    df.drop_duplicates(inplace=True)
    df.fillna("N/A", inplace=True)
    return df

def filter_data(df, column_name, value):
    """Filter rows based on a column value."""
    if column_name in df.columns:
        return df[df[column_name] == value]
    return df  # Return unfiltered if column does not exist

def rename_columns(df, rename_dict):
    """Rename columns based on user-defined mappings."""
    return df.rename(columns=rename_dict)

def convert_units(df, column_name, conversion_factor):
    """Convert numeric values in a column by a given factor."""
    if column_name in df.columns and pd.api.types.is_numeric_dtype(df[column_name]):
        df[column_name] *= conversion_factor
    return df
