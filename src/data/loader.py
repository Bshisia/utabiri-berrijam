import os
from nicegui import ui
import pandas as pd

DATA_PATH = "../data/heart.csv"

def load_data():
    """
    Load data from a CSV file.

    This function checks if the data file exists at the specified path.
    If the file exists, it reads the data into a pandas DataFrame and returns it.
    If the file does not exist or an error occurs during loading, it notifies the user and returns None.

    Returns:
        pd.DataFrame: The loaded data as a pandas DataFrame, or None if an error occurs.
    """
    try:
        if not os.path.exists(DATA_PATH):
            ui.notify(f"Error: Data file not found at {DATA_PATH}", type="negative")
            return None
        return pd.read_csv(DATA_PATH)
    except Exception as ex:
        ui.notify(f"Error loading data: {ex}", type="negative")
        return None

def create_age_groups(df):
    """
    Create age groups in the data.

    This function creates age groups based on predefined bins and labels,
    and adds a new column "Age Group" to the DataFrame.

    Args:
        df (pd.DataFrame): The input data as a pandas DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with the new "Age Group" column.
    """
    try:
        df_copy = df.copy()
        bins = [0, 40, 60, 80, 100]
        labels = ["<40", "40-60", "60-80", ">80"]
        df_copy["Age Group"] = pd.cut(
            df_copy["age"], bins=bins, labels=labels, right=False
        )
        return df_copy
    except Exception as ex:
        ui.notify(f"Error creating age groups: {ex}", type="negative")
        return df