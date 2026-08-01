import streamlit as st
import requests

API_URL = "http://13.200.246.112:8501/predict"

st.title("Insurance Premium Prediction")

st.markdown("Enter your details below to get a predicted insurance premium category.")

age = st.number_input("Age", min_value=1, max_value=119, value=30, step=1)

weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0, step=0.5)

height = st.number_input("Height (in meters)", min_value=0.5, max_value=2.5, value=1.7, step=0.01)

income_lpa = st.number_input("Annual Income (in Lakhs)", min_value=0.0, value=10.0, step=0.5)

smoker = st.selectbox("Are you a smoker?", [True, False])

city = st.text_input("City", value="Delhi")

occuppation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium"):
    input_data = {
        'age': age,
        'weight': weight,
        'height': height,
        'income_lpa': income_lpa,
        'smoker': smoker,
        'city': city,
        'occuppation': occuppation
    }

    try:
        response = requests.post(API_URL, json=input_data)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Insurance Premium Category: {result['response']}")
        else:
            st.error(f"API Error {response.status_code}: {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the API. Make sure your FastAPI server is running on http://13.200.246.112:8501/predict")