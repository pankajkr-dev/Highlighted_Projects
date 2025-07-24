import streamlit as st
from twilio.rest import Client

# Hardcoded Twilio credentials
# Use your own Twilio Credentials
account_sid = ""
auth_token = ""
twilio_number = ""

# TwiML URL that tells Twilio what to say during the call
twiml_url = "http://demo.twilio.com/docs/voice.xml"

st.title("Make a Phone Call")

# Input for recipient number
recipient_number = st.text_input("Enter the recipient's phone number (e.g., +91XXXXXXXXXX)")

# Button to trigger the call
if st.button("Make Call"):
    if not recipient_number:
        st.warning("Please enter a phone number.")
    else:
        try:
            client = Client(account_sid, auth_token)
            call = client.calls.create(
                to=recipient_number,
                from_=twilio_number,
                url=twiml_url
            )
            st.success("Call initiated!")
        except Exception as e:
            st.error(f"Failed to make the call: {e}")
