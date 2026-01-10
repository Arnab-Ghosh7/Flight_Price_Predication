import os

from src.data.make_dataset import load_data
from src.features.build_features import build_features
from src.models.train_model import train_and_save_best_model
from src.visualization.visualize import plot_model_errors


def main():
    print("🚀 Starting Flight Price Prediction Pipeline")

    # Ensure folders exist
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("reports/figures", exist_ok=True)

    # Step 1: Load raw data
    df = load_data()
    print("✅ Raw data loaded")

    # Step 2: Feature Engineering
    df_processed = build_features(df)
    print("✅ Feature engineering completed")

    # Step 3: Save preprocessed data
    processed_path = "data/processed/preprocessed_data.csv"
    df_processed.to_csv(processed_path, index=False)
    print(f"📦 Preprocessed data saved at: {processed_path}")

    # Step 4: Train models & save best one
    y_test, y_pred, best_model = train_and_save_best_model(df_processed)
    print(f"✅ Best model trained: {best_model}")

    # Step 5: Save & display evaluation graphs
    plot_model_errors(y_test, y_pred)

    print("\n🎉 Pipeline executed successfully!")


if __name__ == "__main__":
    main()
