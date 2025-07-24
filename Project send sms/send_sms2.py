
import streamlit as st
from twilio.rest import Client

# Twilio credentials
account_sid = ""
auth_token = ""
verify_service_sid = ""  # Replace with your Verify Service SID

client = Client(account_sid, auth_token)

st.title("Twilio Phone Number Verifier")

# Step 1: Enter phone number
phone_number = st.text_input("Enter phone number to verify (e.g., +91XXXXXXXXXX)")

if st.button("Send Verification Code"):
    try:
        verification = client.verify.services(verify_service_sid).verifications.create(
            to=phone_number,
            channel="sms"
        )
        st.success(f" Verification code sent to {phone_number}")
    except Exception as e:
        st.error(f" Failed to send code: {e}")

# Step 2: Enter verification code
verification_code = st.text_input("Enter the verification code you received")

if st.button("Verify Code"):
    try:
        check = client.verify.services(verify_service_sid).verification_checks.create(
            to=phone_number,
            code=verification_code
        )
        if check.status == "approved":
            st.success("Phone number verified successfully!")
        else:
            st.warning("Verification failed. Please check the code and try again.")
    except Exception as e:
        st.error(f"Failed to verify code: {e}")
