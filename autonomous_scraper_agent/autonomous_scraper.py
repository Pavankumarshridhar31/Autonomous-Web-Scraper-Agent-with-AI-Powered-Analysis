import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import openai
import streamlit as st

# OpenAI API key
openai.api_key = st.secrets.get("OPENAI_API_KEY", "sk-proj-D3oB3rtu380349848398434538TRuQVMvvOckeRcnpEJAUoA")

def scrape_page(url):
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for s in soup(["script", "style"]):
            s.extract()
        text = soup.get_text(separator="\n")
        links = [urljoin(url, a["href"]) for a in soup.find_all("a", href=True)]
        links = [l for l in links if l.startswith("http")]
        return text.strip(), links
    except Exception as e:
        return f"Error scraping {url}: {e}", []

def analyze_with_llm(text, query):
    prompt = f"""
You are an AI agent analyzing scraped webpages.

Webpage content (truncated): 
{text[:3000]}

Task: {query}

Provide a clear, structured result.
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI web scraping assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"LLM Error: {e}"

def autonomous_scraper(start_url, query, depth=1, max_links=3):
    visited = set()
    results = {}
    def crawl(url, level):
        if url in visited or level > depth:
            return
        visited.add(url)
        text, links = scrape_page(url)
        if text:
            analysis = analyze_with_llm(text, query)
            results[url] = analysis
        for link in links[:max_links]:
            crawl(link, level + 1)
    crawl(start_url, 0)
    return results

st.set_page_config(page_title="Autonomous Web Scraper Agent", layout="wide")
st.title("🤖 Autonomous Web Scraper Agent with LLM")
url = st.text_input("🔗 Enter a URL to scrape", "https://en.wikipedia.org/wiki/Artificial_intelligence")
query = st.text_area("📝 Task for the Agent", "Summarize the main points in bullet form.")
depth = st.slider("🌐 Crawl Depth", 0, 2, 1)
max_links = st.slider("🔗 Max Links Per Page", 1, 10, 3)
if st.button("🚀 Run Agent"):
    with st.spinner("Scraping and analyzing..."):
        results = autonomous_scraper(url, query, depth=depth, max_links=max_links)
    st.success("✅ Analysis Complete!")
    for page, analysis in results.items():
        with st.expander(f"🌍 {page}"):
            st.markdown(analysis)
