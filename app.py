from flask import Flask, render_template, request
import pandas as pd
import joblib

from src.features.build_features import build_features

app = Flask(__name__)

MODEL_PATH = "models/best_model.pkl"


# Load trained model once
model = joblib.load(MODEL_PATH)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect form data
        input_data = {
            "Airline": request.form["Airline"],
            "Date_of_Journey": request.form["Date_of_Journey"],
            "Source": request.form["Source"],
            "Destination": request.form["Destination"],
            "Route": request.form["Route"],
            "Dep_Time": request.form["Dep_Time"],
            "Arrival_Time": request.form["Arrival_Time"],
            "Duration": request.form["Duration"],
            "Total_Stops": request.form["Total_Stops"],
            "Additional_Info": request.form["Additional_Info"]
        }

        # Convert to DataFrame
        df = pd.DataFrame([input_data])

        # Apply SAME feature engineering as training
        df_processed = build_features(df)

        # Predict price
        prediction = model.predict(df_processed)[0]

        return render_template(
            "index.html",
            prediction_text=f"Estimated Flight Price: ₹ {round(prediction, 2)}"
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error occurred: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)
