import streamlit as st
import subprocess
import os

st.set_page_config(page_title="🌐 HTTrack Downloader", page_icon="🧲")
st.title("🧲 Full Website Downloader (HTTrack)")

# 📥 Input fields
url = st.text_input("Enter website URL", placeholder="https://example.com")
output_folder = st.text_input("Output folder name", value="site_backup")

# 🧲 Run HTTrack
if st.button("Download Website"):
    if not url.strip():
        st.warning("⚠️ Please enter a valid URL.")
    else:
        with st.spinner("Mirroring website..."):
            try:
                command = [
                    "httrack",
                    url,
                    "-O", output_folder,
                    "--mirror",
                    "--convert-links",
                    "--adjust-extension",
                    "--page-requisites",
                    "--no-parent"
                ]
                subprocess.run(command, check=True)
                st.success(f"✅ Website downloaded to '{output_folder}'")
                st.balloons()
            except Exception as e:
                st.error(f"❌ Error during download:\n{e}")

# 📂 Show downloaded files
if os.path.exists(output_folder):
    with st.expander("📁 View downloaded files"):
        files = os.listdir(output_folder)
        st.write(files if files else "No files found yet.")
