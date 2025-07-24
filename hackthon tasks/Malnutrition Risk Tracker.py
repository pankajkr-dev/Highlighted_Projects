import streamlit as st
import pandas as pd

st.set_page_config(page_title="Malnutrition Tracker", page_icon="🍎")

st.title("🍎 Child Malnutrition Risk Tracker")

name = st.text_input("Child's Name")
age = st.slider("Age (in years)", 0, 10)
weight = st.number_input("Weight (kg)", 5.0, 30.0)
height = st.number_input("Height (cm)", 50.0, 150.0)

if st.button("Check Risk"):
    bmi = weight / ((height / 100) ** 2)
    st.write(f"**BMI:** {bmi:.2f}")
    if bmi < 14:
        st.error("⚠️ High Risk of Malnutrition")
    elif bmi < 16:
        st.warning("⚠️ Moderate Risk")
    else:
        st.success("✅ Healthy")

    # Save record
    record = pd.DataFrame([{
        "Name": name,
        "Age": age,
        "Weight": weight,
        "Height": height,
        "BMI": round(bmi, 2)
    }])
    record.to_csv("malnutrition_records.csv", mode='a', header=not os.path.exists("malnutrition_records.csv"), index=False)

if os.path.exists("malnutrition_records.csv"):
    st.subheader("📋 Recent Records")
    st.dataframe(pd.read_csv("malnutrition_records.csv").tail(5))
