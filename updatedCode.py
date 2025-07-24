import streamlit as st
import speech_recognition as sr
import pyttsx3

# ---------- Apply Custom CSS ----------
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
        color: #22223b;
    }
    .main {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 14px;
        box-shadow: 0 4px 16px rgba(17,75,138,0.07);
    }
    h1, h2, h3 {
        color: #114b8a;
        font-family: 'Segoe UI', 'Arial', sans-serif;
        letter-spacing: 1px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #114b8a 0%, #5bc0be 100%);
        color: #fff;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        margin-top: 1em;
        font-weight: 600;
        border: none;
        box-shadow: 0 2px 8px rgba(91,192,190,0.08);
        transition: background 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #5bc0be 0%, #114b8a 100%);
    }
    .stTextInput>div>input, .stNumberInput>div>input {
        border-radius: 8px;
        padding: 0.5em;
        border: 1px solid #5bc0be;
        background-color: #f0f4f8;
        color: #22223b;
    }
    .stSelectbox>div>div>div {
        border-radius: 8px;
        border: 1px solid #5bc0be;
        background-color: #f0f4f8;
        color: #22223b;
    }
    .stForm {
        padding: 14px;
        background: linear-gradient(90deg, #eef3fa 60%, #e0fbfc 100%);
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(17,75,138,0.04);
    }
    .stAlert {
        border-radius: 8px !important;
        font-weight: 500;
    }
    .stSuccess {
        background-color: #e6fffa !important;
        color: #114b8a !important;
    }
    .stError {
        background-color: #ffe6e6 !important;
        color: #d7263d !important;
    }
    .stWarning {
        background-color: #fffbe6 !important;
        color: #fbb13c !important;
    }
    /* Make Expense History section text black */
    .history-black, .history-black * {
        color: #000 !important;
    }
    /* Make Transaction History section text black */
    .transaction-black, .transaction-black * {
        color: #000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Voice Output Function ----------
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# ---------- Session State Initialization ----------
if "users" not in st.session_state:
    st.session_state.users = {}
    st.session_state.balances = {}
    st.session_state.transactions = {}
    st.session_state.expenses = {}

st.title("Simple Wallet & Expense Tracker")

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
    st.subheader(f"Hello, {username}")
    st.write(f"**Balance:** ₹{balance:.2f}")

    st.header("Wallet")
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

    st.header("Transactions")
    for i, (act, amt) in enumerate(st.session_state.transactions[username], 1):
        st.write(f"{i}. {act}: ₹{amt:.2f}")

    st.header("Add Expense")
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

    st.header("Expense History")
    for e in st.session_state.expenses[username]:
        st.write(f"{e['category']} - {e['description']} - ₹{e['amount']:.2f}")

    st.header("Voice Input")
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
