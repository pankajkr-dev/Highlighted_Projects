import streamlit as st
import speech_recognition as sr
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



if "users" not in st.session_state:
    st.session_state.users = {}
    st.session_state.balances = {}
    st.session_state.transactions = {}
    st.session_state.expenses = {}

st.title(" Simple Wallet & Expense Tracker")


username = st.sidebar.text_input("Enter your username")

if username:
    if username not in st.session_state.users:
        
        st.session_state.users[username] = True
        st.session_state.balances[username] = 0.0
        st.session_state.transactions[username] = []
        st.session_state.expenses[username] = []
        st.sidebar.success("Account created!")
    else:
        st.sidebar.success("Welcome back!")

    balance = st.session_state.balances[username]
    st.subheader(f" Hello, {username}")
    st.write(f" Balance: ₹{balance:.2f}")

    
    st.header(" Wallet")
    action = st.selectbox("Choose", ["Deposit", "Withdraw"])
    amount = st.number_input("Amount (₹)", min_value=0.0, step=1.0)

    if st.button("Submit"):
        if action == "Deposit":
            st.session_state.balances[username] += amount
            st.success(f"Deposited ₹{amount:.2f}")
        elif amount <= balance:
            st.session_state.balances[username] -= amount
            st.success(f"Withdrew ₹{amount:.2f}")
        else:
            st.error("Insufficient funds")

        st.session_state.transactions[username].append((action, amount))

    
    st.header(" Transactions")
    for i, (act, amt) in enumerate(st.session_state.transactions[username], 1):
        st.write(f"{i}. {act}: ₹{amt:.2f}")

    
    st.header(" Add Expense")
    with st.form("expense_form"):
        category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Other"])
        description = st.text_input("Description")
        expense = st.number_input("Amount (₹)", min_value=0.0, step=1.0)
        submit = st.form_submit_button("Add Expense")

        if submit:
            if expense <= st.session_state.balances[username]:
                st.session_state.balances[username] -= expense
                st.session_state.expenses[username].append({
                    "category": category,
                    "description": description,
                    "amount": expense
                })
                st.success("Expense added!")
            else:
                st.error("Not enough balance")

    
    st.header(" Expense History")
    for e in st.session_state.expenses[username]:
        st.write(f"{e['category']} - {e['description']} - ₹{e['amount']:.2f}")

    
    st.header(" Voice Input")
    if st.button("Speak Now"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("Listening...")
            try:
                audio = recognizer.listen(source, timeout=5)
                text = recognizer.recognize_google(audio)
                st.success(f"You said: {text}")
                speak(f"You said: {text}")
            except sr.UnknownValueError:
                st.error("Could not understand.")
                speak("Sorry, I could not understand that.")
            except sr.RequestError:
                st.error("Service error.")
                speak("There was a problem with the service.")
else:
    st.warning("Please enter a username to start.")