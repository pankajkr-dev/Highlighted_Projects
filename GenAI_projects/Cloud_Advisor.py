import streamlit as st
import google.generativeai as genai

# 🎯 Configure Gemini API
genai.configure(api_key="AIzaSyCb_6m_-Yszgpj_MEKmubcjKNS_pBA7kTE")

# 💬 Define your intelligent chatbot prompt
def get_cloud_advice(user_input):
    model = genai.GenerativeModel("gemini-2.5-flash")
    chat = model.start_chat()

    prompt = f"""
Act as an intelligent cloud solution advisor helping non-technical users.

If someone asks a plain-English question like: "{user_input}"

Respond by:
1. Suggesting the best cloud service or solution (AWS, Azure, GCP etc.)
2. Estimating cost or pricing model in simple terms
3. Explaining how long it takes to implement
4. Mentioning big companies using this service
5. Sharing 1 helpful tutorial or official documentation link

Your reply should be clear, friendly, and easy to understand for beginners.
"""

    response = chat.send_message(prompt)
    return response.text

# 🖼️ Streamlit App UI
st.set_page_config(page_title="Cloud Advisor Chatbot", page_icon="☁️")

st.title("☁️ Cloud Solution Advisor")
st.markdown("Ask a cloud-related question in plain English. No tech jargon needed!")

# 📥 Input field
user_query = st.text_input("💬 What's your cloud question?", placeholder="e.g., How do I speed up my website?")

# ▶️ Trigger chatbot
if user_query and st.button("🧠 Get Cloud Advice"):
    with st.spinner("Thinking..."):
        answer = get_cloud_advice(user_query)
        st.success("✅ Cloud Advisor's Response:")
        st.markdown(answer)
