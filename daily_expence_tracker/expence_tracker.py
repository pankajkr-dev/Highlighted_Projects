import streamlit as st

# Set initial budget
INITIAL_BUDGET = 2000.0

st.title("Monthly Budget Expense Tracker")

# Initialize session state for expenses and remaining money
if "expenses" not in st.session_state:
    st.session_state.expenses = []
if "remaining" not in st.session_state:
    st.session_state.remaining = INITIAL_BUDGET

# Show remaining money
st.subheader(f"Remaining Balance: {st.session_state.remaining:.2f}")

# Input form
date = st.date_input("Date")
category = st.text_input("Category")
amount = st.number_input("Amount", min_value=0.0)
description = st.text_input("Description")

# Add expense button
if st.button("Add Expense"):
    if amount > st.session_state.remaining:
        st.error("Not enough balance! You can't afford this expense.")
    elif st.session_state.remaining == 0:
        st.warning("You’ve already spent all your money.")
    else:
        st.session_state.expenses.append({
            "Date": date,
            "Category": category,
            "Amount": amount,
            "Description": description
        })
        st.session_state.remaining -= amount
        st.success("Expense added!")

# Display all expenses
if st.session_state.expenses:
    st.write("### All Expenses")
    for i, exp in enumerate(st.session_state.expenses, 1):
        st.write(f"{i}. {exp['Date']} | {exp['Category']} | ₹{exp['Amount']} - {exp['Description']}")
else:
    st.info("No expenses recorded yet.")

# Final message if budget is exhausted
if st.session_state.remaining == 0:
    st.warning("You've spent your entire 2000 budget for the month")
