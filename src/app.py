import streamlit as st
import pandas as pd
import joblib

model = joblib.load("Best Random Credit Model.pkl")

st.title("Credit Risk Application App")
st.write("Enter Applicant information")

# ------------------------
# Manual Encoding Maps
# ------------------------
sex_map = {"male": 1, "female": 0}

housing_map = {"own": 0, "rent": 1, "free": 2}

saving_map = {
    "little": 0,
    "moderate": 1,
    "rich": 2,
    "quite rich": 3
}

checking_map = {
    "little": 0,
    "moderate": 1,
    "rich": 2
}

# ------------------------
# Inputs
# ------------------------
age = st.number_input("Age", min_value=18, max_value=100, value=35)
job = st.number_input("Job (0-3)", min_value=0, max_value=3, value=1)
sex = st.selectbox("Sex", ["male", "female"])
housing = st.selectbox("Housing", ["own", "rent", "free"])
credit_amount = st.number_input("Credit amount", min_value=0, value=5000)
saving_accounts = st.selectbox("Saving accounts", ["little", "moderate", "rich", "quite rich"])
checking_account = st.selectbox("Checking account", ["little", "moderate", "rich"])
duration = st.number_input("Duration (month)", min_value=1, value=12)

# ------------------------
# Create Input DataFrame
# ------------------------
input_df = pd.DataFrame([{
    "Age": age,
    "Job": job,
    "Sex": sex_map[sex],
    "Housing": housing_map[housing],
    "Credit amount": credit_amount,
    "Saving accounts": saving_map[saving_accounts],
    "Checking account": checking_map[checking_account],
    "Duration": duration,
}])

# ------------------------
# Prediction
# ------------------------
if st.button("Predict risk"):
    pred = model.predict(input_df)[0]

    if pred == 1:
        st.success("Congrats! You are eligible for loan")
    else:
        st.error("Sorry! We can't give you loan just now")
# st.write("Model features:", list(model.feature_names_in_))
# st.write("Input features:", list(input_df.columns))