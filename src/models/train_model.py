import os
import joblib
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor


def train_and_save_best_model(df):

    X = df.drop("Price", axis=1)
    y = df["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0
    )

    models = {
        "LinearRegression": LinearRegression(),
        "Ridge": Ridge(alpha=1.0),
        "Lasso": Lasso(alpha=0.001),
        "RandomForest": RandomForestRegressor(
            n_estimators=200,
            random_state=42,
            n_jobs=-1
        ),
        "GradientBoosting": GradientBoostingRegressor(
            random_state=42
        )
    }

    best_model = None
    best_model_name = None
    best_r2 = -np.inf
    best_predictions = None

    print("\n🔍 Model Evaluation Results\n")

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

        r2 = r2_score(y_test, preds)
        rmse = np.sqrt(mean_squared_error(y_test, preds))

        print(f"{name} → R2: {r2:.4f}, RMSE: {rmse:.2f}")

        if r2 > best_r2:
            best_r2 = r2
            best_model = model
            best_model_name = name
            best_predictions = preds

    os.makedirs("models", exist_ok=True)
    joblib.dump(best_model, "models/best_model.pkl")

    print("\n✅ Best Model Saved")
    print(f"Model: {best_model_name}")
    print(f"R2 Score: {best_r2:.4f}")

    return y_test, best_predictions, best_model_name
