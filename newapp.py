import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Page Title
st.title("Crop Yield Prediction using Linear Regression")

# Sample Dataset
# Convert all values from per hectare to per acre (1 hectare = 2.47105 acres)
data = {
    'Rainfall (mm)': [200, 150, 180, 220, 160, 190, 210, 170, 250, 230],
    'Temperature (°C)': [25, 28, 24, 23, 27, 26, 22, 29, 21, 20],
    'Soil pH': [6.5, 6.8, 7.0, 6.7, 6.2, 6.4, 7.2, 6.3, 6.9, 6.6],
    'Fertilizer (kg/acre)': [val / 2.47105 for val in [100, 90, 110, 95, 85, 105, 115, 80, 120, 100]],
    'Yield (kg/acre)': [val / 2.47105 for val in [3000, 2800, 3200, 3100, 2700, 3300, 3400, 2600, 3500, 3250]]
}
df = pd.DataFrame(data)

# Show Data
st.subheader(" Sample Data")
st.dataframe(df)

# Train Model
X = df[['Rainfall (mm)', 'Temperature (°C)', 'Soil pH', 'Fertilizer (kg/acre)']]
y = df['Yield (kg/acre)']
model = LinearRegression()
model.fit(X, y)

# User Inputs
st.subheader("Enter Crop Conditions")
rainfall = st.slider('Rainfall (mm)', 100, 300, 200)
temperature = st.slider('Temperature (°C)', 15, 35, 25)
soil_ph = st.slider('Soil pH', 5.0, 8.0, 6.5)
fertilizer = st.slider('Fertilizer (kg/acre)', 50, 150, 100)

# Predict Button
if st.button("Predict Yield"):
    input_data = np.array([[rainfall, temperature, soil_ph, fertilizer]])
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Crop Yield: {prediction:.2f} kg/acre")
