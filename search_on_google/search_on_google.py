from googlesearch import search
import requests
from bs4 import BeautifulSoup

def google_search_and_extract(query, num_results=5):
    print(f"🔍 Searching for: {query}\n")
    try:
        results = search(query, num_results=num_results)
        for i, url in enumerate(results, start=1):
            print(f"{i}. URL: {url}")
            try:
                response = requests.get(url, timeout=5)
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.title.string.strip() if soup.title else "No title found"
                print(f"   📝 Title: {title}\n")
            except Exception as e:
                print(f"   ⚠️ Could not retrieve title: {e}\n")
    except Exception as e:
        print(f"❌ Search failed: {e}")

# 🔧 Customize your search query here
query = "DevOps automation tools 2025"

google_search_and_extract(query)
