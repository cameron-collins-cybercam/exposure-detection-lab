import requests

def fetch_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None
