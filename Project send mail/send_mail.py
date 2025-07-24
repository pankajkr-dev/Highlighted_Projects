import streamlit as st
import smtplib
from email.message import EmailMessage

# Streamlit UI
st.title("Email Sender")

sender_email = st.text_input("Your Gmail address")
receiver_email = st.text_input("Recipient's Gmail address")
subject = st.text_input("Subject")
message_body = st.text_area("Message")

# Hardcoded App Password (make sure to keep this secure!)
APP_PASSWORD = "krhf aplf rzgr beor"

if st.button("Send Email"):
    if not all([sender_email, receiver_email, subject, message_body]):
        st.warning("Please fill in all fields.")
    else:
        try:
            # Compose the email
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = sender_email
            msg["To"] = receiver_email
            msg.set_content(message_body)

            # Connect to Gmail SMTP server
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(sender_email, APP_PASSWORD)
                smtp.send_message(msg)

            st.success("✅ Email sent successfully!")
        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")