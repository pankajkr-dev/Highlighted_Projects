import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Smart Agriculture", page_icon="🌾")

st.title("🌾 Smart Agriculture Dashboard")

# Simulated sensor data
data = {
    "Time": ["6 AM", "9 AM", "12 PM", "3 PM", "6 PM"],
    "Soil Moisture (%)": [random.randint(30, 60) for _ in range(5)],
    "Temperature (°C)": [random.randint(25, 35) for _ in range(5)]
}
df = pd.DataFrame(data)

st.line_chart(df.set_index("Time"))

# Crop suggestion
moisture = df["Soil Moisture (%)"].mean()
temp = df["Temperature (°C)"].mean()

st.subheader("🌱 Crop Suggestion")
if moisture > 45 and temp < 32:
    st.success("Suggested Crop: Rice 🌾")
elif moisture < 40:
    st.info("Suggested Crop: Millet 🌿")
else:
    st.warning("Suggested Crop: Maize 🌽")
