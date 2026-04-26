import streamlit as st
import pandas as pd
import numpy as np
import pickle

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --- 1. Load your exported files ---
try:
    model = pickle.load(open('baseline_model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
except FileNotFoundError:
    st.error("Missing .pkl files! Place baseline_model.pkl and scaler.pkl in this folder.")

st.title("Simple Churn Predictor")
st.write("Enter basic customer details to predict churn risk.")

# --- 2. User Inputs ---
col1, col2 = st.columns(2)

with col1:
    tenure = st.number_input("Tenure (Months)", value=12)
    monthly_charges = st.number_input("Monthly Charges ($)", value=50.0)
    total_charges = st.number_input("Total Charges ($)", value=500.0)

with col2:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])

# --- 3. Prediction Logic ---
if st.button("Predict Now"):
    # Convert text to numbers (Manual Label Encoding)
    gender_bin = 1 if gender == "Male" else 0
    senior_bin = 1 if senior == "Yes" else 0
    partner_bin = 1 if partner == "Yes" else 0
    dependents_bin = 1 if dependents == "Yes" else 0

    # Create the feature list (7 inputs)
    current_inputs = [
        gender_bin, senior_bin, partner_bin, dependents_bin, 
        tenure, monthly_charges, total_charges
    ]
    
    # Fill the remaining 12 features with 0 to satisfy the 19-feature Scaler
    # This acts as a 'dummy' filler for columns like Contract, TechSupport, etc.
    full_feature_list = current_inputs + [0] * 39
    
    # Convert to array and shape for the model
    raw_features = np.array([full_feature_list])
    
    # Scale and Predict
    try:
        scaled_features = scaler.transform(raw_features)
        prediction = model.predict(scaled_features)
        
        st.divider()
        if prediction[0] == 1:
            st.error("### Result: High Risk of Churn")
        else:
            st.success("### Result: Low Risk / Likely to Stay")
            
    except Exception as e:
        st.error(f"Prediction Error: {e}")