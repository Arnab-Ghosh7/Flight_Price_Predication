import os
import matplotlib.pyplot as plt
import seaborn as sns


def plot_model_errors(y_test, y_pred):
    """
    Save and display model evaluation plots.
    """

    # Create directory if it doesn't exist
    os.makedirs("reports/figures", exist_ok=True)

    # -------- Error Distribution --------
    plt.figure(figsize=(6, 4))
    sns.histplot(y_test - y_pred, kde=True)
    plt.title("Prediction Error Distribution")
    plt.xlabel("Error")

    error_dist_path = "reports/figures/error_distribution.png"
    plt.savefig(error_dist_path, bbox_inches="tight")
    plt.show()
    plt.close()

    # -------- Actual vs Predicted --------
    plt.figure(figsize=(6, 4))
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")
    plt.title("Actual vs Predicted Price")

    scatter_path = "reports/figures/actual_vs_predicted.png"
    plt.savefig(scatter_path, bbox_inches="tight")
    plt.show()
    plt.close()

    print("📊 Graphs saved:")
    print(f" - {error_dist_path}")
    print(f" - {scatter_path}")
