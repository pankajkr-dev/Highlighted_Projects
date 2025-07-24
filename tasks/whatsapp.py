import streamlit as st
import pywhatkit as kit
import datetime

st.title("WhatsApp Message Sender")

phone = st.text_input("Enter recipient phone number (with country code, e.g. +919876543210):", value="+919587831158")
message = st.text_area("Enter your message:")
send_now = st.checkbox("Send now (in 1 minute)?")

if not send_now:
  hour = st.number_input("Hour (24h format):", min_value=0, max_value=23, value=datetime.datetime.now().hour)
  minute = st.number_input("Minute:", min_value=0, max_value=59, value=(datetime.datetime.now().minute + 2) % 60)
else:
  now = datetime.datetime.now()
  hour = 17
  minute = 20
  minute = (now.minute + 1) % 60

if st.button("Send Message"):
  if phone and message:
    try:
      kit.sendwhatmsg(phone, message, int(hour), int(minute), wait_time=10)
      st.success(f"Message scheduled to {phone} at {hour:02d}:{minute:02d}")
    except Exception as e:
      st.error(f"Failed to send message: {e}")
  else:
    st.warning("Please enter both phone number and message.")

st.info("Note: This will open WhatsApp Web in your browser and requires your WhatsApp to be logged in.")