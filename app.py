import streamlit as st
import pandas as pd
import joblib

# Load the model (no scaler needed since you trained on raw data)
model = joblib.load("credit_risk_model.pkl")

# Title and description
st.title("Credit Risk Assessment")
st.write("Enter your financial details to see your loan approval odds.")

# Input form (matching your dataset columns)
fico_range_low = st.number_input("FICO Credit Score", min_value=300, max_value=850, value=700)
annual_inc = st.number_input("Annual Income ($)", min_value=0.0, value=48000.0)
dti = st.number_input("Debt-to-Income Ratio (%)", min_value=0.0, max_value=100.0, value=20.0)
loan_amnt = st.number_input("Loan Amount ($)", min_value=0.0, value=9000.0)
revol_bal = st.number_input("Revolving Balance ($)", min_value=0.0, value=5000.0)

# Predict button
if st.button("Predict Approval Odds"):
    # Create a DataFrame from inputs, matching your dataset order and column names
    input_data = pd.DataFrame({
        'fico_range_low': [fico_range_low],
        'annual_inc': [annual_inc],
        'dti': [dti],
        'loan_amnt': [loan_amnt],
        'revol_bal': [revol_bal]
    })

    # Predict probability (class 1 = Approved, class 0 = Not Approved)
    prob = model.predict_proba(input_data)[0][1]  # Probability of approval

    # Display result
    st.success(f"Your loan approval odds: {prob:.2%}")

# Optional: Add a note for your portfolio
st.write("Built with LendingClub data by [Your Name] for portfolio purposes.")