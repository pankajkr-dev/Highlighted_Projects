import streamlit as st
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup

# Page config
st.set_page_config(page_title="Gemini Web Scraper", page_icon="")

st.title("Gemini-Powered Web Page Q&A")
st.markdown("Scrape a webpage and ask questions about its content using Gemini.")

# Configure Gemini
genai.configure(api_key="AIzaSyCb_6m_-Yszgpj_MEKmubcjKNS_pBA7kTE")

# Step 1: Input URL
url = st.text_input("Enter a website URL", placeholder="https://example.com")

# Step 2: Scrape the webpage
scraped_text = ""
if url:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        scraped_text = soup.get_text(separator=" ", strip=True)
        scraped_text = scraped_text[:3000]  # Gemini token limit
        st.success("Page scraped successfully!")
        with st.expander("View Scraped Content"):
            st.write(scraped_text)
    except Exception as e:
        st.error(f"Error scraping the URL: {e}")

# Step 3: Input question
user_question = st.text_area("Ask a question based on the webpage")

# Step 4: Send to Gemini
if scraped_text and user_question and st.button("Get Answer"):
    model = genai.GenerativeModel("gemini-2.5-flash")
    chat = model.start_chat()

    message = f"""
    Here is some content from a web page:

    \"\"\"{scraped_text}\"\"\"

    Now answer this question: {user_question}
    """

    with st.spinner("Thinking..."):
        response = chat.send_message(message)
        st.subheader("🤖 Gemini's Answer:")
        st.write(response.text)
