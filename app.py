import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")

import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import ui
import logging
import joblib
import os

# Configure logging
logging.basicConfig(
    filename='app.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Set page config first (must be first Streamlit command)
st.set_page_config(
    page_title="Credit Risk Assessment",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define expected columns after one-hot encoding (all 25 features)
expected_columns = [
    'annual_inc', 'dti', 'fico_range_low', 'loan_amnt', 'revol_bal', 'term', 'emp_length',
    'home_ownership_MORTGAGE', 'home_ownership_NONE', 'home_ownership_OTHER', 'home_ownership_OWN', 
    'home_ownership_RENT', 'purpose_credit_card', 'purpose_debt_consolidation', 'purpose_educational',
    'purpose_home_improvement', 'purpose_house', 'purpose_major_purchase', 'purpose_medical',
    'purpose_moving', 'purpose_other', 'purpose_renewable_energy', 'purpose_small_business',
    'purpose_vacation', 'purpose_wedding'
]

# Initialize session state
if 'prediction_made' not in st.session_state:
    st.session_state.prediction_made = False
if 'approval_odds' not in st.session_state:
    st.session_state.approval_odds = None
if 'model_loaded' not in st.session_state:
    st.session_state.model_loaded = False

def load_model_and_scaler():
    """Load the model and scaler with proper error handling"""
    try:
        # Load the ANN model
        model = tf.keras.models.load_model("final_ann_model.h5")
        # Load the scaler
        scaler = joblib.load("minmax_scaler.pkl")
        st.session_state.model_loaded = True
        return model, scaler
    except Exception as e:
        logging.error(f"Error loading model or scaler: {e}")
        st.error(f"⚠️ Error loading model or scaler: {e}")
        st.stop()

def preprocess_inputs(inputs):
    """Convert user inputs to model-ready format"""
    # Mappings for categorical variables
    term_mapping = {'36 months': 36, '60 months': 60}
    emp_length_mapping = {
        '< 1 year': 0, '1 year': 1, '2 years': 2, '3 years': 3, '4 years': 4,
        '5 years': 5, '6 years': 6, '7 years': 7, '8 years': 8, '9 years': 9,
        '10+ years': 10
    }
    
    # Create DataFrame with numeric features
    input_data = pd.DataFrame({
        'annual_inc': [inputs["annual_inc"]],
        'dti': [inputs["dti"]],
        'fico_range_low': [inputs["fico_range_low"]],
        'loan_amnt': [inputs["loan_amnt"]],
        'revol_bal': [inputs["revol_bal"]],
        'term': [term_mapping[inputs["term"]]],
        'emp_length': [emp_length_mapping[inputs["emp_length"]]]
    })
    
    # Create one-hot encoding for home_ownership
    for col in ['MORTGAGE', 'NONE', 'OTHER', 'OWN', 'RENT']:
        col_name = f'home_ownership_{col}'
        input_data[col_name] = 1 if inputs["home_ownership"] == col else 0
    
    # Create one-hot encoding for purpose
    purposes = [
        'credit_card', 'debt_consolidation', 'educational', 'home_improvement', 
        'house', 'major_purchase', 'medical', 'moving', 'other', 
        'renewable_energy', 'small_business', 'vacation', 'wedding'
    ]
    for purpose in purposes:
        col_name = f'purpose_{purpose}'
        input_data[col_name] = 1 if inputs["purpose"] == purpose else 0
    
    # Ensure all expected columns are present and in the correct order
    for col in expected_columns:
        if col not in input_data.columns:
            input_data[col] = 0
    input_data = input_data[expected_columns]
    
    return input_data

def validate_inputs(inputs):
    """Validate user inputs and return a list of errors"""
    errors = []
    if inputs["annual_inc"] <= 0:
        errors.append("Annual Income must be greater than 0")
    if inputs["loan_amnt"] <= 0:
        errors.append("Loan Amount must be greater than 0")
    if inputs["dti"] < 0 or inputs["dti"] > 100:
        errors.append("Debt-to-Income Ratio must be between 0 and 100")
    if inputs["fico_range_low"] < 300 or inputs["fico_range_low"] > 850:
        errors.append("FICO score must be between 300 and 850")
    if inputs["revol_bal"] < 0:
        errors.append("Revolving Balance cannot be negative")
        
    return errors

def predict_approval_odds(input_data, model, scaler):
    """Make prediction using the loaded model and scaler"""
    # Scale the input data
    input_scaled = scaler.transform(input_data)
    
    # Make prediction with ANN
    prob = model.predict(input_scaled, verbose=0)[0][0]
    return prob

def main():
    """Main app function"""
    logging.info("Starting the Credit Risk Assessment app...")
    
    # Apply custom UI
    ui.apply_custom_css()
    
    try:
        # Load model and scaler if not already loaded
        if not st.session_state.model_loaded:
            model, scaler = load_model_and_scaler()
        else:
            model, scaler = load_model_and_scaler()  # Reload each time for now (in production would store in session_state)
        
        # Create layout
        ui.create_header()
        
        # Create tabs
        tab1, tab2, tab3 = st.tabs(["📊 Assessment", "🔍 How It Works", "ℹ️ About"])
        
        with tab1:
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # Get user inputs
                inputs = ui.create_input_form()
                
                # Predict button
                predict_clicked = st.button("Predict Approval Odds", type="primary", use_container_width=True)
                
                if predict_clicked:
                    # Validate inputs
                    errors = validate_inputs(inputs)
                    if errors:
                        for error in errors:
                            st.error(f"⚠️ {error}")
                    else:
                        with st.spinner("Calculating your approval odds..."):
                            try:
                                # Preprocess inputs
                                input_data = preprocess_inputs(inputs)
                                
                                # Make prediction
                                prob = predict_approval_odds(input_data, model, scaler)
                                
                                # Store in session state
                                st.session_state.prediction_made = True
                                st.session_state.approval_odds = prob
                                
                                logging.info(f"Prediction successful: {prob:.2%}")
                                
                                # Force rerun to update UI
                                st.experimental_rerun()
                                
                            except Exception as e:
                                logging.error(f"Prediction error: {e}")
                                st.error(f"⚠️ Prediction error: {e}")
                                st.write("Technical details:", str(e))
            
            with col2:
                ui.create_results_section()
                
                # Debug info (only visible in development environment)
                if os.environ.get('ENVIRONMENT') == 'development':
                    with st.expander("Debug Information", expanded=False):
                        if 'input_data' in locals():
                            st.write("Model input shape:", input_data.shape)
                            st.write("Model input columns:", input_data.columns.tolist())
        
        with tab2:
            ui.create_how_it_works_tab()
        
        with tab3:
            ui.create_about_tab()
            
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        st.error(f"An unexpected error occurred: {e}")
        st.write(f"Error details: {e}")

if __name__ == "__main__":
    main()