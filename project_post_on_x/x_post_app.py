import streamlit as st
import tweepy

# Directly embedded Twitter API credentials
# Note: Replace these with your actual credentials
# For security reasons, it's recommended to use environment variables or a secure vault for sensitive information.
consumer_key = "miE7dlgtGc"
consumer_secret = "RZhyQ7g8S03f"
access_token = "EgAaKU40ME3Rqa2E1U5"
access_token_secret = "qdsnevblVAcx"

# Tweepy v2 Client setup
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Streamlit UI
st.set_page_config(page_title="Post to X", page_icon="✉️")
st.title("Post to X with Python")

tweet_text = st.text_area("Write your tweet:", max_chars=280)

if st.button("Post Tweet"):
    if not tweet_text.strip():
        st.warning("Tweet text cannot be empty.")
    else:
        try:
            response = client.create_tweet(text=tweet_text)
            tweet_id = response.data["id"]
            tweet_url = f"https://x.com/user/status/{tweet_id}"
            st.success(f"Tweet posted successfully!\n[View Tweet]({tweet_url})")
        except Exception as e:
            st.error(f"Failed to post tweet:\n{e}")
