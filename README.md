# Credit Risk Modelling App

## Overview

This project implements an end-to-end machine learning system for predicting credit risk using customer financial data. The model is trained on structured data and deployed via a **Streamlit application** for real-time inference.

The workflow separates:

* **Model development** (notebook)
* **Model usage** (app)

---

## Project Structure

```
.
├── data/
│   └── german_credit_data.csv
│
├── models/                        # Generated locally (not tracked in Git)
│   ├── model.pkl
│   ├── encoders.pkl
│   └── scaler.pkl
│
├── notebooks/
│   └── credit_risk.ipynb         # Model training and experimentation
│
├── src/
│   └── app.py                    # Streamlit application
│
├── requirements.txt
└── README.md
```

---

## Important Note

The trained model and preprocessing artifacts (`.pkl` files) are **not included in the repository**.

They must be generated before running the application.

---

## Setup & Usage

### Step 1: Train Model (Required)

Run the notebook:

```
jupyter notebook notebooks/credit_risk.ipynb
```

Execute all cells to generate:

* `models/model.pkl`
* `models/encoders.pkl`
* `models/scaler.pkl`

---

### Step 2: Run Application

```
streamlit run src/app.py
```

This will launch a web interface for predicting credit risk.

---

## Machine Learning Pipeline

### Data Preprocessing

* Encoding categorical variables
* Feature scaling

### Model Training

* Trained classification model (e.g., Random Forest)
* Model selected based on performance

### Deployment

* Streamlit-based UI for real-time predictions

---

## Author

Mainak Jana
