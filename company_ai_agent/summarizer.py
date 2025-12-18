import re

# -------------------------------
# Cleaning
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# -------------------------------
# Sentence extraction
# -------------------------------
def extract_sentences(text, min_len=80, max_count=5):
    sentences = re.split(r"\. |\n", text)
    clean = []

    for s in sentences:
        s = s.strip()
        if len(s) >= min_len:
            clean.append(s.capitalize())
        if len(clean) == max_count:
            break

    return clean


# -------------------------------
# Company overview filter (NEW)
# -------------------------------
COMPANY_KEYWORDS = [
    "company", "platform", "organization", "provides",
    "offers", "builds", "develops", "solutions", "services"
]

FEATURE_KEYWORDS = [
    "integration", "workflow", "action", "pull request",
    "issue", "api", "documentation", "tutorial", "how to"
]

def extract_company_overview(text):
    sentences = re.split(r"\. |\n", text)
    selected = []

    for s in sentences:
        s_clean = s.strip().lower()

        if len(s_clean) < 80:
            continue

        # Reject feature / docs sentences
        if any(k in s_clean for k in FEATURE_KEYWORDS):
            continue

        # Accept company-level sentences
        if any(k in s_clean for k in COMPANY_KEYWORDS):
            selected.append(s.strip().capitalize())

        if len(selected) == 3:
            break

    return selected


# -------------------------------
# Main summarizer
# -------------------------------
def summarize_company(pages: dict):
    home = clean_text(pages.get("home", ""))
    about = clean_text(pages.get("about", ""))
    products_page = clean_text(pages.get("products", ""))
    policies_page = clean_text(pages.get("policies", ""))

    # -------------------------------
    # What the company does (FIXED)
    # -------------------------------
    overview_source = about if len(about) > 200 else home
    overview_sentences = extract_company_overview(overview_source)

    if overview_sentences:
        overview = " ".join(overview_sentences)
    else:
        overview = (
            "The company operates as a technology-focused organization that provides "
            "products and services based on publicly available information from its website."
        )

    # -------------------------------
    # Products / Services
    # -------------------------------
    product_keywords = [
        "copilot", "actions", "codespaces", "security",
        "platform", "tool", "service", "software"
    ]

    products = set()
    for k in product_keywords:
        if k in products_page:
            products.add(k.capitalize())

    # -------------------------------
    # Brand positioning / uniqueness
    # -------------------------------
    positioning_keywords = ["ai", "developer", "enterprise", "open source"]

    positioning = []
    for k in positioning_keywords:
        if k in overview_source:
            positioning.append(f"Focus on {k}-driven solutions")

    if not positioning:
        positioning.append("Technology-focused organization")

    # -------------------------------
    # Public policies
    # -------------------------------
    policies = []
    if "privacy" in policies_page:
        policies.append("Privacy Policy")
    if "terms" in policies_page:
        policies.append("Terms of Service")

    # -------------------------------
    # Build final output
    # -------------------------------
    output = []

    output.append("## What the Company Does")
    output.append(overview)
    output.append("")

    output.append("## Products / Services")
    if products:
        for p in sorted(products):
            output.append(f"- {p}")
    else:
        output.append("- Details available on the official website")
    output.append("")

    output.append("## Brand Positioning / Uniqueness")
    for p in positioning[:3]:
        output.append(f"- {p}")
    output.append("")

    output.append("## Public Policies")
    if policies:
        for p in policies:
            output.append(f"- {p}")
    else:
        output.append("- No explicit public policies found")

    return "\n".join(output)
