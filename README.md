# Flight Price Prediction

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Arnab-Ghosh7/Flight_Price_Predication?style=flat)](https://github.com/Arnab-Ghosh7/Flight_Price_Predication/stargazers)

---

## 📖 Overview

**Flight Price Prediction** is a comprehensive, end-to-end machine learning solution designed to address the unpredictability of airfare prices. Airline ticket costs fluctuate significantly due to demand, seasonality, route complexity, and airline-specific dynamics. This project aims to bring transparency to these fluctuations by providing users with accurate, data-driven price estimates.

Built with a robust Python ecosystem, the application leverages historical flight data to train advanced regression models. It features a complete production pipeline—from raw data ingestion and extensive feature engineering to model serialization and deployment via a **Flask** web interface.

**Key Highlights:**
- **Full-Stack ML Pipeline:** Orchestrates data loading, cleaning, transformation, and model training in a modular fashion.
- **Advanced Feature Engineering:** Extracts rich insights from timestamps (e.g., journey day/month, departure times) and complex categorical data (routes, stops).
- **Interactive Web UI:** Users can input specific travel details (Airline, Source, Destination, Stops, etc.) into a clean web form to get instant price predictions.
- **Reproducible Data Science:** Includes `Makefile` commands, `requirements.txt`, and clear directory structures to ensure the analysis can be easily reproduced.

---

## Table of Contents

- [🚀 Quick Start](#-quick-start)
- [🗂 Project Structure](#-project-structure)
- [⚙️ Installation](#-installation)
- [🔧 Usage](#-usage)
  - [Run the pipeline](#run-the-pipeline)
  - [Start the Flask app](#start-the-flask-app)
- [📊 Features & Engineering](#-features--engineering)
- [📁 Data](#-data)
- [🧠 Modeling](#-modeling)
- [📈 Visualisation](#-visualisation)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/Arnab-Ghosh7/Flight_Price_Predication
cd Flight_Price_Predication

# Create a virtual environment (optional but recommended)
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the data pipeline (creates processed data & trains the model)
python run_pipeline.py

# Launch the web UI
python app.py
```

Open your browser at `http://127.0.0.1:5000` and start predicting!

---

## 🗂 Project Structure

```
Flight_Price_Predication
├── .env                     # Environment variables (if needed)
├── .gitignore
├── LICENSE
├── Makefile                 # Helpful shortcuts (e.g., `make data`)
├── README.md                # **You are here**
├── data
│   ├── external             # Third‑party raw data
│   ├── raw                  # Original immutable data dump (Excel files)
│   ├── interim              # Intermediate transformations
│   └── processed            # Clean CSV ready for modelling
├── docs                     # Sphinx documentation (optional)
├── models                   # Serialized models & predictions
├── notebooks                # Exploratory Jupyter notebooks
├── references               # Data dictionaries & manuals
├── reports                  # Generated analysis reports
│   └── figures              # Plots & figures used in reports
├── requirements.txt         # Python dependencies
├── setup.py                 # Installable package configuration
├── src
│   ├── __init__.py
│   ├── data
│   │   └── make_dataset.py # Loads raw Excel data into a DataFrame
│   ├── features
│   │   └── build_features.py # Feature engineering pipeline
│   ├── models
│   │   ├── train_model.py   # Model training & selection logic
│   │   └── predict_model.py # Helper for inference (used by Flask app)
│   └── visualization
│       └── visualize.py    # Plots model error distributions
├── app.py                   # Flask web service exposing `/` and `/predict`
├── run_pipeline.py          # Orchestrates data loading → feature engineering → training → reporting
└── tox.ini                  # Test automation configuration
```

---

## ⚙️ Installation

1. **Python** – The project is tested on Python 3.9+. Install from the official site if you don’t have it.
2. **Dependencies** – All required packages are listed in `requirements.txt`. Install them with:
   ```bash
   pip install -r requirements.txt
   ```
3. **Optional – Development tools** – If you plan to contribute, install the development extras:
   ```bash
   pip install -e .[dev]
   ```
   This will also install `tox` for running the test suite.

---

## 🔧 Usage

### Run the pipeline

The pipeline script `run_pipeline.py` performs the full end‑to‑end workflow:
```bash
python run_pipeline.py
```
It will:
- Load the raw training data (`data/raw/Data_Train.xlsx`).
- Apply the feature engineering defined in `src/features/build_features.py`.
- Save the processed CSV to `data/processed/preprocessed_data.csv`.
- Train several regression models, select the best based on validation performance, and persist it to `models/best_model.pkl`.
- Generate error plots saved under `reports/figures/`.

### Start the Flask app

After the model is trained, launch the web UI:
```bash
python app.py
```
Visit `http://127.0.0.1:5000` and fill in the flight details. The app will:
- Accept the form data, convert it to a DataFrame.
- Run the same feature engineering pipeline used during training.
- Load the persisted model (`models/best_model.pkl`).
- Return an estimated price.

---

## 📊 Features & Engineering

The `build_features.py` module extracts and encodes the following information:
- **Date components** – Day, month, year.
- **Time components** – Arrival and departure hour/minute.
- **Stop count** – Normalised to an integer.
- **Route splits** – Up to five intermediate airports.
- **Categorical encoding** – Airline, source, destination, additional info, and each route segment are label‑encoded.
- **Redundant columns** – Original raw columns (e.g., `Date_of_Journey`, `Dep_Time`, `Arrival_Time`, `Duration`, `Route`) are dropped after transformation.

---

## 📁 Data

- **Raw data** – `data/raw/Data_Train.xlsx` contains the original training set with the target column `Price`.
- **Processed data** – After running the pipeline, a clean CSV (`data/processed/preprocessed_data.csv`) is produced, ready for any downstream experiments.

---

## 🧠 Modeling

`src/models/train_model.py` (not shown here) implements a simple model‑selection loop that evaluates multiple regressors (e.g., Linear Regression, Random Forest, XGBoost). The model achieving the lowest validation RMSE is serialized as `models/best_model.pkl`.

---

## 📈 Visualisation

`src/visualization/visualize.py` creates diagnostic plots such as:
- **Prediction vs. Actual**
- **Residual distribution**
- **Feature importance** (if supported by the chosen model)

All figures are saved under `reports/figures/` and are referenced in the generated reports.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b my-feature`).
3. Make your changes and ensure the test suite passes (`tox`).
4. Submit a Pull Request with a clear description of the changes.

Please adhere to the existing code style (PEP 8) and include unit tests for new functionality.

---

## 📜 License

This project is licensed under the **MIT License** – see the `LICENSE` file for details.

---

## 👤 Author

- **Arnab Ghosh**   

## 🙏 Acknowledgements

- Project scaffold generated from the **Cookiecutter Data Science** template.
- Inspired by publicly available flight‑price datasets and Kaggle competitions.
- Thanks to the open‑source community for the libraries that make this work possible (Flask, pandas, scikit‑learn, etc.).

---


