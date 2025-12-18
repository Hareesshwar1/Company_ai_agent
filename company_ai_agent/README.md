Company Information AI Agent
Overview

This project is a small AI-style agent that collects publicly available information from a company’s website and produces a clean, structured summary.

Given a company URL, the agent looks for relevant public pages such as Home, About, Products/Services, and Policies, extracts useful information from those pages, and generates a readable Markdown report covering:

HERE I USED THE GITHUB URL= https://www.github.com/

What the company does

Products or services offered

Brand positioning or uniqueness

Public policies (if available)

The entire solution was built to fit within a one-day scope, using only public data, without requiring logins or paid APIs.

Architecture

The project is organized into three simple components:

scraper.py:
Responsible for fetching public web pages, extracting visible text, and identifying relevant internal links.

main.py:
Acts as the controller for the pipeline. It coordinates scraping, groups pages into categories (home, about, products, policies), and sends the collected content to the summarizer.

summarizer.py:
It cleans and filters the extracted text, applies rule-based heuristics to identify company-level information, and generates a structured Markdown output (output.md).

Approach

The agent takes a company website URL as input.

It scrapes the homepage along with a limited number of relevant internal pages.

Pages are categorized based on their purpose using simple URL patterns.

A rule based summarization approach extracts organizational level of  information.

The final result is written as a structured Markdown summary.

This approach keeps the system easy to understand, deterministic, and extendable.

Limitations:
The summarizer relies on heuristics, so for large or documentation-heavy websites, the overview may reflect mission statements or initiatives rather than a concise business description.

Semantic understanding is limited compared to LLM-based solutions.

JavaScript heavy websites may expose less content through basic HTML scraping.

Future Improvements

With additional time, the following improvements could be made:

Integrating an LLM-based summarizer for better semantic understanding.

Using browser automation tools such as Playwright or Selenium for dynamic websites.

Improving page classification using NLP-based techniques instead of URL patterns.

Constraints Compliance

This solution fully respects the given constraints:

Only publicly available data is used

No authentication or login is required

No paid APIs are involved

The task was completed within one working day

Output

The agent generates a structured Markdown report (output.md) containing the summarized company information.