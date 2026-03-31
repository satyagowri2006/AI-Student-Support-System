import requests
from bs4 import BeautifulSoup
from googlesearch import search


def google_search(query, num_results=3):

    urls = []

    for url in search(query + " site:vignan.ac.in", num_results=num_results):
        urls.append(url)

    return urls


def extract_web_content(url):

    try:
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = " ".join([p.get_text() for p in paragraphs])

        return text[:2000]

    except:
        return ""