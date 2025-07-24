import streamlit as st
import geocoder
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Public Safety Alert", page_icon="🚨")

st.title("🚨 Public Safety Alert System")
emergency_types = ["Crime", "Fire", "Medical", "Natural Disaster", "Other"]
emergency = st.selectbox("Select Emergency Type", emergency_types)
description = st.text_area("Describe the situation", max_chars=300)

g = geocoder.ip('me')
location = g.latlng if g.ok else [None, None]

if st.button("Send Alert"):
    if not description.strip():
        st.warning("Please enter a description.")
    elif not location[0]:
        st.error("Could not fetch location.")
    else:
        alert = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": emergency,
            "description": description,
            "latitude": location[0],
            "longitude": location[1]
        }
        df = pd.DataFrame([alert])
        df.to_csv("alerts.csv", mode='a', header=not os.path.exists("alerts.csv"), index=False)
        st.success("🚨 Alert sent successfully!")
        st.map(df[['latitude', 'longitude']])

if os.path.exists("alerts.csv"):
    st.subheader("📋 Recent Alerts")
    st.dataframe(pd.read_csv("alerts.csv").tail(5))
