import streamlit as st
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Email Sender")

st.title("Email Sender")
st.markdown("Securely send an email using Gmail App Password.")

# Input fields
sender_email = st.text_input("Your Gmail address", placeholder="you@gmail.com")
receiver_email = st.text_input("Recipient's Gmail address", placeholder="recipient@gmail.com")
subject = st.text_input("Subject")
message_body = st.text_area("Message")

APP_PASSWORD = "oomz txtb dhmg jgpp"

# Send Button
if st.button("Send Email"):
    if not all([sender_email, receiver_email, subject, message_body]):
        st.warning("Please fill in all fields.")
    else:
        try:
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = sender_email
            msg["To"] = receiver_email
            msg.set_content(message_body)

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(sender_email, APP_PASSWORD)
                smtp.send_message(msg)

            st.success("Email sent successfully!")
        except smtplib.SMTPAuthenticationError:
            st.error("Authentication failed. Check your Gmail address and App Password.")
        except Exception as e:
            st.error(f"Something went wrong: {e}")
