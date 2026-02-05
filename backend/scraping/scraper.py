import requests
from bs4 import BeautifulSoup
from models import save_headlines

def fetch_bbc_headlines():
    url = "https://www.bbc.com/news"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    headlines = []

    for tag in soup.select("h3"):
        text = tag.get_text(strip=True)
        if text and len(text) > 25:  
            headlines.append(text)

    return headlines

if __name__ == "__main__":
    headlines = fetch_bbc_headlines()
    items = [{"title": h, "url": "https://www.bbc.com/news"} for h in headlines]
    save_headlines("BBC", items)
    print(f"Saved {len(items)} headlines from BBC")