import streamlit as st
import subprocess
import os
import zipfile
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# Gemini setup (use your actual key)
genai.configure(api_key="AIzaSyBbcp-RdyJpZlceQesWy22-Q4nQe1LazJQ")

# Streamlit config
st.set_page_config(page_title="Website Downloader + Gemini Chat")
st.title("Mirror Websites + Ask Gemini")
st.caption("Download websites with HTTrack/curl, then chat with Gemini about the content.")

# User Inputs
url = st.text_input("Website URL", placeholder="https://example.com")
folder_name = st.text_input("Folder name", value="site_backup")

# Validate URL
def is_url_reachable(u):
    try:
        return requests.head(u, timeout=5).status_code < 400
    except:
        return False

# HTTrack Downloader with spoofed User-Agent
def run_httrack(u, f):
    cmd = [
        "httrack", u,
        "-O", f,
        "--mirror",
        "--convert-links",
        "--adjust-extension",
        "--page-requisites",
        "--no-parent",
        "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    ]
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr
    except Exception as e:
        return False, str(e)

# curl fallback
def run_curl(u, f):
    try:
        os.makedirs(f, exist_ok=True)
        out_file = os.path.join(f, "index.html")
        subprocess.run(["curl", "-L", u, "-o", out_file], check=True)
        return True, out_file
    except Exception as e:
        return False, str(e)

# Zip folder
def zip_folder(path):
    zip_name = f"{path}.zip"
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(path):
            for file in files:
                z.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), path))
    return zip_name

# Folder summary
def folder_summary(path):
    count = sum(len(files) for _, _, files in os.walk(path))
    size = sum(os.path.getsize(os.path.join(root, file))
               for root, _, files in os.walk(path) for file in files)
    return count, round(size / 1024, 2)

# Gemini-powered Q&A
def ask_gemini(prompt, html_path):
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, "html.parser")
            content = soup.get_text(separator="\n")
        model = genai.GenerativeModel("gemini-1.5-pro")
        chat = model.start_chat()
        response = chat.send_message(f"{prompt}\n\nBased on this page:\n{content}")
        return response.text
    except Exception as e:
        return f"Gemini error: {e}"

# Begin process
if st.button("Download Website"):
    if not url.strip():
        st.warning("Enter a valid URL.")
    elif not is_url_reachable(url):
        st.error("URL unreachable.")
    else:
        with st.spinner("📡 Attempting HTTrack..."):
            success, output = run_httrack(url, folder_name)

        if success and os.path.exists(folder_name):
            st.success(f"HTTrack finished: `{folder_name}`")
        else:
            st.warning(" HTTrack failed. Trying curl...")
            curl_success, curl_output = run_curl(url, folder_name)
            if curl_success:
                st.success(f"curl downloaded homepage to `{folder_name}/index.html`")
            else:
                st.error(f"curl failed:\n{curl_output}")

        # Summary
        if os.path.exists(folder_name):
            count, size = folder_summary(folder_name)
            st.info(f"{count} files {size} KB")

            # Zip Option
            if st.checkbox("Create .zip archive"):
                zip_path = zip_folder(folder_name)
                st.success(f"Zipped to `{zip_path}`")

            # Homepage preview
            index = os.path.join(folder_name, "index.html")
            if os.path.exists(index):
                st.subheader("Homepage Preview")
                with open(index, "r", encoding="utf-8") as f:
                    html = f.read()
                st.components.v1.html(html, height=600, scrolling=True)
            else:
                st.warning("No index.html available for preview.")

# Gemini Chat Section
index_path = os.path.join(folder_name, "index.html")
if os.path.exists(index_path):
    st.header("Ask Gemini About the Page")
    query = st.text_input("Your question", placeholder="What is this site about?")
    if query:
        with st.spinner("Gemini is reading the page..."):
            answer = ask_gemini(query, index_path)
            st.chat_message("Gemini").markdown(answer)
