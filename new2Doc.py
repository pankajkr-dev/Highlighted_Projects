import streamlit as st
import speech_recognition as sr

# Styling
st.markdown("""
<style>
.main-title { font-size:36px; font-weight:bold; color:#32CD32; text-align:center; margin-bottom:20px; }
.stButton>button { background-color:#4CAF50; color:white; border-radius:8px; padding:8px 20px; border:none; }
.stButton>button:hover { background-color:#45a049; }
.stTextInput>div>div>input { border-radius:8px; border:2px solid #ddd; }
.sidebar .sidebar-content { background-color:#f7f7f7; }
</style>""", unsafe_allow_html=True)
st.markdown('<div class="main-title">💼 Wallet and Expense Tracker</div>', unsafe_allow_html=True)

# Session state
for key in ['users', 'expenses', 'transactions']:
    if key not in st.session_state:
        st.session_state[key] = {}

# User login
username = st.sidebar.text_input("Enter your username")
if username:
    if username not in st.session_state.users:
        st.session_state.users[username] = 0.0
        st.session_state.expenses[username] = []
        st.session_state.transactions[username] = []
        st.sidebar.success(f"New account created for {username}")
    else:
        st.sidebar.success(f"Welcome, {username}")

    balance = st.session_state.users[username]
    st.subheader(f"Hello, {username}")
    st.write(f"Current Balance: ₹{balance:.2f}")

    # Wallet actions
    st.header("Wallet Actions")
    action = st.selectbox("Choose an action", ["Deposit", "Withdraw"])
    amount = st.number_input("Enter amount (₹)", min_value=0.0, step=0.01)

    if st.button("Submit"):
        if action == "Deposit":
            st.session_state.users[username] += amount
            st.session_state.transactions[username].append(("Deposit", amount))
            st.success(f"Deposited ₹{amount:.2f}")
        elif amount <= balance:
            st.session_state.users[username] -= amount
            st.session_state.transactions[username].append(("Withdraw", amount))
            st.success(f"Withdrew ₹{amount:.2f}")
        else:
            st.error("Not enough balance")
    st.write(f"Updated Balance: ₹{st.session_state.users[username]:.2f}")

    # Transaction history
    st.header("Transaction History")
    for i, (t, a) in enumerate(st.session_state.transactions[username], 1):
        st.write(f"{i}. {t} - ₹{a:.2f}") if st.session_state.transactions[username] else st.write("No transactions yet")

    # Expense tracker
    st.header("Add Expense")
    with st.form("expense_form"):
        cat = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Utilities", "Other"])
        desc = st.text_input("Description")
        amt = st.number_input("Expense Amount (₹)", min_value=0.0, step=0.01)
        if st.form_submit_button("Add Expense") and amt <= st.session_state.users[username]:
            st.session_state.expenses[username].append({"category": cat, "description": desc, "amount": amt})
            st.session_state.users[username] -= amt
            st.success(f"Expense of ₹{amt:.2f} added")
        elif amt > st.session_state.users[username]:
            st.error("Not enough balance for this expense")

    # Expense history
    st.header("Expense History")
    for e in st.session_state.expenses[username]:
        st.write(f"{e['category']} - {e['description']} - ₹{e['amount']:.2f}") if st.session_state.expenses[username] else st.write("No expenses yet")

    # Reset
    if st.button("Reset Account"):
        for key in ['users', 'expenses', 'transactions']:
            st.session_state[key][username] = 0.0 if key == 'users' else []
        st.success("Your account has been reset")
else:
    st.warning("Please enter a username to start")

# Voice Input
st.header("Voice Input")
if st.button("🎙 Speak Now"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak something!")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            st.success(f"Recognized Text: {text}")
        except sr.UnknownValueError:
            st.error("Sorry, could not understand your speech.")
        except sr.RequestError:
            st.error("Speech Recognition service is unavailable at the moment.")
