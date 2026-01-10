import pandas as pd


def load_data():
    """
    Load training dataset containing the target variable (Price).
    """
    df = pd.read_excel("data/raw/Data_Train.xlsx")
    return df
