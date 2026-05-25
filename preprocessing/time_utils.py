import pandas as pd

def convert_to_datetime(df, columns):
    for col in columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    return df

def calculate_duration(df, dep_col, arr_col):
    df["duration_hours"] = (
        (df[arr_col] - df[dep_col]).dt.total_seconds() / 3600
    )
    df["duration_hours"].fillna(df["duration_hours"].median(), inplace=True)
    return df