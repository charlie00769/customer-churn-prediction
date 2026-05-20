import streamlit as st
import pickle
import numpy as np

# =========================
# Load Model, Scaler, Columns
# =========================
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

# =========================
# UI
# =========================
st.set_page_config(page_title="Churn Predictor")
st.title("📊 Customer Churn Prediction")

# =========================
# Inputs
# =========================
account_length = st.number_input("Account Length")
customer_service_calls = st.number_input("Customer Service Calls")

total_day_minutes = st.number_input("Day Minutes")
total_day_calls = st.number_input("Day Calls")
total_day_charge = st.number_input("Day Charge")

total_eve_minutes = st.number_input("Evening Minutes")
total_eve_calls = st.number_input("Evening Calls")
total_eve_charge = st.number_input("Evening Charge")

total_night_minutes = st.number_input("Night Minutes")
total_night_calls = st.number_input("Night Calls")
total_night_charge = st.number_input("Night Charge")

total_intl_minutes = st.number_input("Intl Minutes")
total_intl_calls = st.number_input("Intl Calls")
total_intl_charge = st.number_input("Intl Charge")

intl_plan = st.selectbox("International Plan", ["No", "Yes"])
voice_mail_plan = st.selectbox("Voice Mail Plan", ["No", "Yes"])

intl_plan = 1 if intl_plan == "Yes" else 0
voice_mail_plan = 1 if voice_mail_plan == "Yes" else 0

# =========================
# Prediction
# =========================
if st.button("Predict"):

    try:
        # Create input dictionary
        input_dict = {
            "Account length": account_length,
            "Total day minutes": total_day_minutes,
            "Total day calls": total_day_calls,
            "Total day charge": total_day_charge,
            "Total eve minutes": total_eve_minutes,
            "Total eve calls": total_eve_calls,
            "Total eve charge": total_eve_charge,
            "Total night minutes": total_night_minutes,
            "Total night calls": total_night_calls,
            "Total night charge": total_night_charge,
            "Total intl minutes": total_intl_minutes,
            "Total intl calls": total_intl_calls,
            "Total intl charge": total_intl_charge,
            "Customer service calls": customer_service_calls,
            "International plan_Yes": intl_plan,
            "Voice mail plan_Yes": voice_mail_plan
        }

        # Match column order automatically
        final_input = [input_dict.get(col, 0) for col in columns]

        sample = np.array([final_input])

        # Scale
        sample_scaled = scaler.transform(sample)

        # Predict
        prediction = model.predict(sample_scaled)[0]
        probability = model.predict_proba(sample_scaled)[0][1]

        if prediction == 1:
            st.error(f"❌ Customer will churn\nProbability: {probability:.2f}")
        else:
            st.success(f"✅ Customer will stay\nProbability: {probability:.2f}")

    except Exception as e:
        st.error("Error occurred")
        st.text(str(e))