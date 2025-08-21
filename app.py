import streamlit as st
import requests

# Use the ngrok URL for your FastAPI
API_URL = "https://8366fd1bb989.ngrok-free.app/"

st.title("📊 Customer Churn Prediction (via FastAPI)")

st.sidebar.header("Enter Customer Details")

age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=30)
total_purchase = st.sidebar.number_input("Total Purchase", min_value=0.0, value=1000.0)
account_manager = st.sidebar.selectbox("Has Account Manager?", [0, 1])
years = st.sidebar.number_input("Years with Company", min_value=0.0, value=3.0)
num_sites = st.sidebar.number_input("Number of Sites", min_value=0, value=5)

if st.sidebar.button("Predict Churn"):
    payload = {
        "Age": age,
        "Total_Purchase": total_purchase,
        "Account_Manager": account_manager,
        "Years": years,
        "Num_Sites": num_sites
    }
    try:
        response = requests.post(API_URL, json=payload, timeout=10)
        if response.status_code == 200:
            result = response.json()
            prediction = result.get("churn_prediction")
            probability = result.get("churn_probability")
            st.subheader("🔮 Prediction Result")
            if prediction == 1:
                st.error(f"❌ Customer likely to churn (Probability: {probability:.2f})")
            else:
                st.success(f"✅ Customer will stay (Probability: {probability:.2f})")
        else:
            st.error(f"⚠ API Error: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"❌ Request failed: {e}")
