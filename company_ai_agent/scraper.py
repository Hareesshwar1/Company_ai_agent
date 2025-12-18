import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_text_from_url(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    # remove junk
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    text = " ".join(soup.stripped_strings)
    return text


def find_relevant_links(base_url):
    response = requests.get(base_url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    keywords = ["about", "service", "product", "privacy", "policy"]
    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"].lower()
        if any(word in href for word in keywords):
            full_url = urljoin(base_url, a["href"])
            links.add(full_url)

    return list(links)
