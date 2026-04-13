from langchain.tools import tool 
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os 
from dotenv import load_dotenv
from rich import print

try:
    import streamlit as st
except ImportError:
    st = None

load_dotenv()

def get_secret(name: str) -> str | None:
    value = os.getenv(name)
    if value:
        return value
    if not st:
        return None
    if name in st.secrets:
        return st.secrets[name]
    env_secrets = st.secrets.get("env") if isinstance(st.secrets, dict) else None
    if env_secrets and name in env_secrets:
        return env_secrets[name]
    return None

# Delay TavilyClient initialization until needed
_tavily_client = None

def get_tavily_client():
    global _tavily_client
    if _tavily_client is None:
        api_key = get_secret("TAVILY_API_KEY")
        if not api_key:
            raise ValueError(
                "TAVILY_API_KEY is not set. Please set it in Streamlit secrets or add it to .env "
                "as TAVILY_API_KEY=<value>."
            )
        _tavily_client = TavilyClient(api_key=api_key)
    return _tavily_client

@tool
def web_search(query : str) -> str:
    """Search the web for recent and reliable information on a topic . Returns Titles , URLs and snippets."""
    tavily = get_tavily_client()
    results = tavily.search(query=query,max_results=5)

    out = []

    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )
    
    return "\n----\n".join(out)

@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"
