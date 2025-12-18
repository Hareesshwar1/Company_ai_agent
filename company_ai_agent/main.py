from scraper import extract_text_from_url, find_relevant_links
from summarizer import summarize_company

def run_agent(company_url):
    print("Fetching homepage...")

    page_content = {
        "home": "",
        "about": "",
        "products": "",
        "policies": ""
    }

    # Home page
    page_content["home"] = extract_text_from_url(company_url)

    print("Finding relevant pages...")
    links = find_relevant_links(company_url)[:5]

    for i, link in enumerate(links, start=1):
        print(f"[{i}/{len(links)}] Scraping: {link}")
        text = extract_text_from_url(link)
        lower = link.lower()

        if "about" in lower:
            page_content["about"] += text
        elif "product" in lower or "service" in lower:
            page_content["products"] += text
        elif "privacy" in lower or "terms" in lower or "policy" in lower:
            page_content["policies"] += text
        else:
            page_content["home"] += text

    print("Generating structured summary...")
    summary = summarize_company(page_content)

    with open("output.md", "w", encoding="utf-8") as f:
        f.write(summary)

    print("DONE  Output saved as output.md")

if __name__ == "__main__":
    url = "https://github.com/"
    run_agent(url)
