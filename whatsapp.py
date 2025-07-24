import streamlit as st
import speech_recognition as sr
import pywhatkit
import time

st.title("Voice-Controlled WhatsApp Messenger")

contacts = {
    "Beta": "‪+919113724211‬",
    "Mota": "‪+918690681390‬",
    "Priyanshu vit ": "‪+919973163055‬"
}

if st.button("Start Listening"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak your message")
        audio = r.listen(source)

    command = r.recognize_google(audio)
    st.write("Heard:", command)

    if "to" in command.lower():
        parts = command.lower().split("to")
        message = parts[0].replace("send", "").strip()
        name = parts[1].strip().capitalize()

        if name in contacts:
            st.success(f"Sending '{message}' to {name}")
            pywhatkit.sendwhatmsg_instantly(contacts[name], message)
        else:
            st.error(f"Name '{name}' not found in contacts.")
    else:
        st.warning("Couldn't detect 'to' in your message. Format: send <msg> to <name>")