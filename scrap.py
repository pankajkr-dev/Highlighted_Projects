import requests
from bs4 import BeautifulSoup
from googlesearch import search

query = "Python web scraping"
for url in search(query, num_results=5):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        print(f"🔗 {url}\n📄 Title: {soup.title.string}\n")
    except:
        print(f"❌ Failed to fetch {url}\n")
