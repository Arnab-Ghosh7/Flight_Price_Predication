import pandas as pd
from sklearn.preprocessing import LabelEncoder


def build_features(df: pd.DataFrame) -> pd.DataFrame:

    # Date features
    df["Date"] = df["Date_of_Journey"].str.split("/").str[0].astype(int)
    df["Month"] = df["Date_of_Journey"].str.split("/").str[1].astype(int)
    df["Year"] = df["Date_of_Journey"].str.split("/").str[2].astype(int)
    df.drop("Date_of_Journey", axis=1, inplace=True)

    # Arrival time
    df["Arrival_Time"] = df["Arrival_Time"].str.split(" ").str[0]

    # Stops
    df["Total_Stops"] = df["Total_Stops"].fillna("1 stop")
    df["Total_Stops"] = df["Total_Stops"].replace("non-stop", "0 stop")
    df["Stop"] = df["Total_Stops"].str.split(" ").str[0].astype(int)
    df.drop("Total_Stops", axis=1, inplace=True)

    # Arrival split
    df["Arrival_Hour"] = df["Arrival_Time"].str.split(":").str[0].astype(int)
    df["Arrival_Minute"] = df["Arrival_Time"].str.split(":").str[1].astype(int)
    df.drop("Arrival_Time", axis=1, inplace=True)

    # Departure split
    df["Departure_Hour"] = df["Dep_Time"].str.split(":").str[0].astype(int)
    df["Departure_Minute"] = df["Dep_Time"].str.split(":").str[1].astype(int)
    df.drop("Dep_Time", axis=1, inplace=True)

    # Route features
    df["Route_1"] = df["Route"].str.split("→ ").str[0]
    df["Route_2"] = df["Route"].str.split("→ ").str[1]
    df["Route_3"] = df["Route"].str.split("→ ").str[2]
    df["Route_4"] = df["Route"].str.split("→ ").str[3]
    df["Route_5"] = df["Route"].str.split("→ ").str[4]

    for col in ["Route_1", "Route_2", "Route_3", "Route_4", "Route_5"]:
        df[col] = df[col].fillna("None")

    df.drop(["Route", "Duration"], axis=1, inplace=True)

    # Encode categorical variables
    encoder = LabelEncoder()
    categorical_cols = [
        "Airline", "Source", "Destination",
        "Additional_Info",
        "Route_1", "Route_2", "Route_3", "Route_4", "Route_5"
    ]

    for col in categorical_cols:
        df[col] = encoder.fit_transform(df[col])

    return df
