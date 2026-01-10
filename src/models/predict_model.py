import joblib
import pandas as pd


MODEL_PATH = "models/best_model.pkl"


def predict(df: pd.DataFrame):

    model = joblib.load(MODEL_PATH)

    if "Price" in df.columns:
        df = df.drop("Price", axis=1)

    predictions = model.predict(df)
    return predictions
