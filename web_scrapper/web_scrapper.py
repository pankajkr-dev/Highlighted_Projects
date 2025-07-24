import streamlit as st
import subprocess
import os
import zipfile
import requests

# Streamlit Config
st.set_page_config(page_title="HTTrack + curl Downloader")
st.title("Website Downloader")
st.caption("Mirror websites using HTTrack with browser emulation or fallback to curl.")

# Inputs
url = st.text_input("Website URL", placeholder="https://example.com")
folder_name = st.text_input("Output folder name", value="site_backup")

# Check URL
def is_url_reachable(test_url):
    try:
        return requests.head(test_url, timeout=5).status_code < 400
    except:
        return False

# HTTrack Download
def run_httrack(url, folder):
    cmd = [
        "httrack", url,
        "-O", folder,
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

# curl Fallback
def run_curl(url, folder):
    try:
        os.makedirs(folder, exist_ok=True)
        out_file = os.path.join(folder, "index.html")
        cmd = ["curl", "-L", url, "-o", out_file]
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return True, out_file
    except subprocess.CalledProcessError as e:
        return False, e.stderr
    except Exception as e:
        return False, str(e)

# Zip Folder
def zip_folder(path):
    zip_name = f"{path}.zip"
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, path)
                z.write(full_path, arcname)
    return zip_name

# Folder Summary
def folder_summary(path):
    count = 0
    size = 0
    for root, _, files in os.walk(path):
        for file in files:
            count += 1
            size += os.path.getsize(os.path.join(root, file))
    return count, round(size / 1024, 2)

# Trigger Mirror
if st.button("Download Website"):
    if not url.strip():
        st.warning("Enter a valid URL.")
    elif not is_url_reachable(url):
        st.error("URL unreachable or blocked.")
    else:
        with st.spinner("Attempting HTTrack download..."):
            ht_success, ht_output = run_httrack(url, folder_name)

        if ht_success and os.path.exists(folder_name):
            st.success(f"HTTrack completed: `{folder_name}`")
        else:
            st.warning("HTTrack failed. Trying curl fallback...")
            curl_success, curl_msg = run_curl(url, folder_name)
            if curl_success:
                st.success(f"curl downloaded HTML to `{folder_name}/index.html`")
            else:
                st.error(f"curl failed:\n{curl_msg}")

        # Summary
        if os.path.exists(folder_name):
            count, size = folder_summary(folder_name)
            st.info(f"{count} files {size} KB")

            # Zip Option
            if st.checkbox("Create .zip archive"):
                zip_path = zip_folder(folder_name)
                st.success(f"Folder zipped: `{zip_path}`")

            # Preview Homepage
            index = os.path.join(folder_name, "index.html")
            if os.path.exists(index):
                st.subheader("Homepage Preview")
                with open(index, "r", encoding="utf-8") as f:
                    html = f.read()
                st.components.v1.html(html, height=600, scrolling=True)
            else:
                st.warning("No index.html available for preview.")

# File List Panel
if os.path.exists(folder_name):
    with st.expander("View Downloaded Files"):
        try:
            files = os.listdir(folder_name)
            st.write(files if files else "Folder is empty.")
        except Exception as e:
            st.error(f"Error reading folder: {e}")
