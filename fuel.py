import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("mpg_model.pkl")

st.set_page_config(page_title="Fuel Efficiency Estimator", layout="centered")
st.title("🚗 Vehicle Fuel Efficiency Estimator")
st.markdown("Estimate a car's fuel efficiency (MPG) using engine and vehicle specs.")

# Input fields
cylinders = st.slider("Cylinders", 3, 12, 4)
displacement = st.number_input("Displacement (cc)", 50.0, 500.0, 150.0)
horsepower = st.number_input("Horsepower", 40.0, 250.0, 100.0)
weight = st.number_input("Weight (lbs)", 1500.0, 5000.0, 2500.0)
acceleration = st.number_input("Acceleration (0–60 mph time)", 8.0, 25.0, 15.0)
model_year = st.slider("Model Year", 70, 82, 76)

# Predict
if st.button("Estimate MPG"):
    input_data = np.array([[cylinders, displacement, horsepower, weight, acceleration, model_year]])
    mpg = model.predict(input_data)[0]
    st.success(f"Estimated Fuel Efficiency: **{mpg:.2f} MPG**")
