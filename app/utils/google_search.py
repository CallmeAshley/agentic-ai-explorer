import os
from dotenv import load_dotenv
from serpapi import GoogleSearch

load_dotenv()

SERP_API_KEY = os.getenv("SERPAPI_API_KEY")

def google_search(query: str, num_results: int = 5):
    params = {
        "engine": "google",
        "q": query,
        "num": num_results,
        "api_key": SERP_API_KEY,
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    summaries = []
    for res in results.get("organic_results", []):
        summaries.append({
            "title": res.get("title"),
            "snippet": res.get("snippet"),
            "url": res.get("link")
        })
    return summaries
