# Company_Ai_Agent


#Overview:

This project is a small AI-style agent that collects publicly available information from a company’s website and produces a clean, structured summary.

Given a company URL, the agent looks for relevant public pages such as Home, About, Products/Services, and Policies, extracts useful information from those pages, and generates a readable Markdown report covering:

HERE I USED THE GITHUB URL= https://www.github.com/

#ARCHITECTURE:
┌───────────────┐
│  User Input   │
│ (Company URL) │
└───────┬───────┘
        │
        ▼
┌───────────────────┐
│     main.py       │
│ Orchestration     │
│ - Controls flow   │
│ - Calls modules   │
└───────┬───────────┘
        │
        ▼
┌───────────────────┐
│    scraper.py     │
│ Web Scraping      │
│ - Fetch HTML      │
│ - Extract text    │
│ - Find links      │
└───────┬───────────┘
        │
        ▼
┌───────────────────┐
│  Page Classifier  │
│ (inside main.py)  │
│ - Home            │
│ - About           │
│ - Products        │
│ - Policies        │
└───────┬───────────┘
        │
        ▼
┌───────────────────┐
│  summarizer.py    │
│ Text Processing   │
│ - Clean text      │
│ - Filter noise    │
│ - Rule-based NLP  │
└───────┬───────────┘
        │
        ▼
┌───────────────────┐
│   output.md       │
│ Structured Result │
│ (Markdown file)   │
└───────────────────┘
--------------
Architecture
--------------
The system follows a simple, modular pipeline:

1.scraper.py – Fetches public web pages, extracts visible text, and discovers relevant internal links.
2.main.py – Orchestrates the workflow, classifies pages (home, about, products, policies), and coordinates the pipeline.
3.summarizer.py – Cleans text, applies rule-based heuristics, and generates a structured Markdown output (output.md).
--------------
Approach
--------------
Accepts a company website URL as input and Scrapes the homepage and a limited set of relevant internal pages,Classifies pages using URL patterns

Applies rule based summarization to extract organization-level information

Outputs a structured Markdown summary

This approach keeps the system deterministic, easy to understand, and extensible.
--------------
Assumptions
--------------
Company information is publicly accessible without authentication

Relevant pages can be identified using URL patterns and keywords

A rule-based approach is sufficient within the given time constraints
---------------
Limitations
---------------
1.Heuristic summarization may reflect mission statements for documentation heavy websites
2.Semantic understanding is limited compared to LLM-based approaches
3.JavaScript-heavy websites may expose less content through HTML scraping


The agent generates a structured Markdown report (output.md) containing the summarized company information.
