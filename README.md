# Autonomous Web Scraper Agent with AI-Powered Analysis

## Overview

This project is an **Autonomous Web Scraper Agent** that leverages **OpenAI's LLM** to automatically extract structured insights from any webpage. It features a **Streamlit-based UI**, allowing users to paste a URL and get an AI-analyzed summary, product information, FAQs, or any custom task.

🔗 Live Demo (Render):
https://autonomous-web-scraper-agent-with-ai-0cni.onrender.com

The agent can:

* Scrape text and links from any website
* Recursively follow links up to a configurable depth
* Use an AI model (GPT-4o-mini or GPT-3.5-turbo) to summarize or extract key information
* Display results in a structured format via Streamlit

---

## Features

* **Easy-to-use UI**: Paste a URL and specify the task
* **Autonomous crawling**: Follow links from the starting page automatically
* **LLM-powered extraction**: Summarize content, extract products, people, FAQs, or any custom query
* **Customizable depth and link limit**: Control how deep the agent crawls and number of links per page
* **Streamlit ready**: Works as a web app for easy deployment

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/autonomous_scraper_agent.git
cd autonomous_scraper_agent
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add your OpenAI API key:

* **Option 1 (Streamlit secrets)**: Create a `.streamlit/secrets.toml` file:

```toml
OPENAI_API_KEY = "your_api_key_here"
```

* **Option 2 (direct)**: Replace `YOUR_OPENAI_API_KEY` in `autonomous_scraper.py`

---

## Usage

Run the Streamlit app:

```bash
streamlit run autonomous_scraper.py
```

1. Paste any URL in the input field.
2. Specify the task (e.g., `Summarize`, `Extract products`, `Generate FAQs`).
3. Adjust **crawl depth** and **max links per page**.
4. Click **Run Agent** and view the results.

---

## Deployment

### Streamlit Cloud

1. Push your repository to GitHub
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Deploy the repository
4. Add `OPENAI_API_KEY` in the Secrets section

### Render

1. Create a new Web Service in Render
2. Connect to your GitHub repository
3. Use start command:

```bash
streamlit run autonomous_scraper.py --server.port 10000 --server.address 0.0.0.0
```

4. Add `OPENAI_API_KEY` as an environment variable in Render

---

## Example Tasks

* Summarize the main points in bullet form
* Extract company or organization names
* Generate FAQs based on the page content
* Extract product details (title, price, description, rating)

---

## Folder Structure

```
autonomous_scraper_agent/
├── autonomous_scraper.py   # Main Streamlit app + scraper + LLM
└── requirements.txt       # Dependencies
```

---

## Notes

* Uses `openai==0.28` for compatibility with ChatCompletion
* Configurable parameters:

  * `depth`: How many levels of links to follow
  * `max_links`: Max number of links per page
* LLM truncates page content to 3000 characters for token safety

---

## License

This project is open-source and available under the MIT License.
