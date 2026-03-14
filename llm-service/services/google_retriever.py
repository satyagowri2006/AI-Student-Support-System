"""
google_retriever.py

Search Google and retrieve information from webpages
related to Vignan University.
"""

import requests
from bs4 import BeautifulSoup


def google_search(query: str):
    """
    Search Google for Vignan University related results
    """

    search_url = f"https://www.google.com/search?q={query}+vignan+university"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(search_url, headers=headers, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        results = []

        for link in soup.find_all("a"):

            href = link.get("href")

            if href and "http" in href:

                if "google" not in href:
                    results.append(href)

            if len(results) >= 3:
                break

        return results

    except Exception:
        return []


def extract_web_content(url: str):
    """
    Extract readable text from webpage
    """

    try:

        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove scripts and style tags
        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text(separator=" ")

        return text[:2000]

    except Exception:
        return ""