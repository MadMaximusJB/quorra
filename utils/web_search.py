import requests
from config import GOOGLE_CSE_API_KEY, GOOGLE_CSE_ID

def search_web(query):
    try:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": GOOGLE_CSE_API_KEY,
            "cx": GOOGLE_CSE_ID,
            "q": query
        }
        response = requests.get(url, params=params)
        results = response.json()
        if "items" in results:
            return [item["snippet"] for item in results["items"]]
        else:
            return ["No results found."]
    except Exception as e:
        print(f"Error searching the web: {e}")
        return ["Error occurred while searching the web."]
