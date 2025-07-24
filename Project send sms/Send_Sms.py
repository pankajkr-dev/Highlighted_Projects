import streamlit as st
from twilio.rest import Client

st.title("Send SMS with Twilio")
#Use your own Twilio Credentials
# Hardcoded Twilio credentials
account_sid = ""
auth_token = ""
twilio_number = ""

# Input fields for recipient and message
recipient_number = st.text_input("Recipient Phone Number (e.g., +919876543210)")
message_body = st.text_area("Message")

if st.button("Send SMS"):
    if not all([recipient_number, message_body]):
        st.warning("Please fill in all fields.")
    else:
        try:
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                body=message_body,
                from_=twilio_number,
                to=recipient_number
            )
            st.success(f"Message sent! SID: {message.sid}")
        except Exception as e:
            st.error(f"Failed to send SMS: {e}")
