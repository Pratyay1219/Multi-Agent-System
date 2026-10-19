# 🤖 Multi-Agent Research Assistant

An AI-powered research assistant that automates web research, information extraction, and summarization using a modular multi-agent workflow. Built with Python, LangChain, BeautifulSoup, Tavily API, and Large Language Models (LLMs).

## 🚀 Overview

The **Multi-Agent Research Assistant** is designed to simplify online research by searching multiple web sources, extracting relevant information, and generating concise, structured summaries.

Instead of manually browsing numerous websites, users can provide a research query and let the system automate key stages of the research process.

## ✨ Features

- 🔎 **Automated Web Search:** Retrieves relevant web sources using the Tavily API.
- 🌐 **Web Scraping:** Extracts useful information from accessible web pages using BeautifulSoup.
- 🧠 **Multi-Agent Architecture:** Organizes research tasks into modular components for searching, information processing, and summarization.
- 📝 **AI-Powered Summarization:** Converts collected information into clear and readable research summaries.
- ⚡ **Automated Research Pipeline:** Reduces manual effort by combining search, extraction, and summarization.
- 🔧 **Modular Design:** Supports future enhancements with additional agents, tools, and research capabilities.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | LLM integration and workflow orchestration |
| Tavily API | Web search and source discovery |
| BeautifulSoup | HTML parsing and content extraction |
| Large Language Models | Information processing and summarization |

## 🏗️ System Architecture

```text
           User Research Query
                    |
                    v
           Research Workflow
                    |
                    v
             Search Agent
             (Tavily API)
                    |
                    v
          Information Extraction
           (BeautifulSoup)
                    |
                    v
          Information Processing
                    |
                    v
          Summarization Agent
                  (LLM)
                    |
                    v
           Research Summary
```

The architecture illustrates the intended research pipeline. The actual agents and execution flow depend on the implementation.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version
- Tavily API key
- API key for your configured LLM provider
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/Pratyay1219/Multi-Agent-Research-Assistant.git
cd Multi-Agent-Research-Assistant
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the packages required by your implementation. For example:

```bash
pip install langchain tavily-python beautifulsoup4 python-dotenv
```

Install any additional package required by your selected LLM provider.

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
TAVILY_API_KEY=your_tavily_api_key
LLM_API_KEY=your_llm_api_key
```

Replace the placeholders with your actual API keys. Ensure that the variable names match those used in your Python code.

**Important:** Never commit your `.env` file or expose API keys publicly.

### 5. Run the Application

Execute the main application file:

```bash
python main.py
```

Replace `main.py` with the actual entry-point filename if your project uses a different one.

## 💡 Example Use Case

**Research Query:**

> Research recent developments in renewable energy storage and summarize the key findings.

**Expected Workflow:**

1. Search the web for relevant sources.
2. Retrieve accessible web-page content.
3. Process and organize the extracted information.
4. Use an LLM to generate a concise research summary.
5. Present the findings for further review.

The quality and coverage of the results depend on the available sources, API limits, and the configured language model.

## 📁 Project Structure

A suggested project structure is shown below. Modify it to match your actual repository.

```text
Multi-Agent-Research-Assistant/
│
├── agents/
│   ├── search_agent.py
│   ├── research_agent.py
│   └── summarization_agent.py
│
├── tools/
│   └── web_scraper.py
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🔐 Security and Best Practices

- Store API keys in environment variables.
- Add `.env` and `.venv/` to `.gitignore`.
- Treat scraped web content as untrusted input.
- Verify important claims against the original sources.
- Respect website terms of service, rate limits, and applicable copyright requirements.

## 🔮 Future Improvements

- Add source citations and reference links to generated reports.
- Implement parallel research agents for faster processing.
- Improve error handling, retries, and rate-limit management.
- Add source relevance scoring and summary-quality evaluation.
- Introduce a web interface for interactive research.
- Support exporting research results to PDF or Markdown.
- Add persistent research history and caching.

## 👨‍💻 Author

**Pratyay Das**

- GitHub: [@Pratyay1219](https://github.com/Pratyay1219)
- LinkedIn: [pratyay19](https://linkedin.com/in/pratyay19)

---

⭐ If you find this project interesting, consider starring the repository!

