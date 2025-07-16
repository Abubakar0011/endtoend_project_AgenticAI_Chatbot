# 🤖 Agentic AI Chatbot – End-to-End Project

This project implements a versatile, end-to-end AI chatbot application using **Streamlit** for the user interface and **LangGraph** for orchestrating complex AI agent workflows. It showcases a modular and extensible chatbot capable of handling multiple real-world use cases.

---

## ✨ Features

- **Interactive Streamlit UI** – Clean interface for live chatbot interaction.
- **Modular Architecture** – Clearly structured components for scalability and customization.
- **Multiple Use Cases**:
  - 🔹 **Basic Chatbot** – General-purpose conversational agent.
  - 🔹 **Web-Search Chatbot** – Real-time Q&A using Tavily Search API.
  - 🔹 **AI News Summarizer** – Fetches and summarizes latest AI news.
- **Configurable LLMs** – Easily switch Groq models via dropdown.
- **LangGraph Integration** – State-managed, agentic AI workflows.
- **Secure API Management** – Input keys via environment or Streamlit sidebar.

---

## 🚀 Technologies Used

- **Python 3.9+**
- **Streamlit** – UI framework
- **LangChain** – Core LLM interactions
- **LangGraph** – Agent state orchestration
- **Groq API** – Large Language Models
- **Tavily API** – External web search tool
- `configparser` – Configuration file management

---

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Abubakar0011/endtoend_project_AgenticAI_Chatbot.git
cd Agentic_AI_Chatbot_endtoend_project
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
# Activate:
# macOS/Linux:
source venv/bin/activate
# Windows CMD:
.\venv\Scripts\activate
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

**Option A: .env File (Recommended)**
Create a `.env` file in the root directory:
```dotenv
GROQ_API_KEY="your_groq_api_key_here"
TAVILY_API_KEY="your_tavily_api_key_here"
```

**Option B: Streamlit Sidebar Input**
Enter keys directly in the UI input fields.

🔑 [Get Groq Key](https://console.groq.com/keys) | [Get Tavily Key](https://app.tavily.com/home)

### 5. Optional: Edit Configuration
Modify settings in `src/langgrap_chatbot_app/UI/uiconfifile.ini`:
```ini
[DEFAULT]
PAGE_TITLE = LangGraph: Build Stateful Agentic AI Graph
LLM_OPTIONS = Groq
USECASE_OPTIONS = Basic Chatbot, Chatbot With Web, AI News
GROQ_MODEL_OPTIONS = llama3-8b-8192, llama3-70b-8192, gemma2-9b-it
```

---

## 🚀 Usage

```bash
streamlit run app.py
```

### Interacting with the Chatbot:
- **Select LLM** → Groq
- **Input API Keys** → In sidebar
- **Choose Use Case**:
  - **Basic Chatbot** → Chat freely
  - **Chatbot With Web** → Requires Tavily key; ask real-time questions
  - **AI News** → Choose timeframe (Daily, Weekly, Monthly) and click Fetch

---

## 📂 Project Structure
```
├── app.py                      # Streamlit entry point
├── requirements.txt
└── src/
    └── langgrap_chatbot_app/
        ├── LLMs/
        │   └── groq_llm.py
        ├── Grpah/              # (Typo: should be 'Graph')
        │   └── graph_builder.py
        ├── Nodes/
        │   ├── basic_chatbot_node.py
        │   ├── chatbot_with_tool.py
        │   └── news_node.py
        ├── State/
        │   └── state.py
        ├── Tools/
        │   └── search_tool.py
        ├── UI/
        │   └── streamlitui/
        │       ├── display_result.py
        │       └── loadui.py
        │   ├── uiconfifile.ini
        │   └── uiconfigfile.py
        └── main.py             # Central control
```

---

## 🧩 Troubleshooting

| Error | Solution |
|-------|----------|
| `ModuleNotFoundError` | Activate virtual environment + `pip install -r requirements.txt` |
| `AttributeError: 'NoneType' object has no attribute 'split'` | Check spelling of config keys in `.ini` file |
| `Graph setup failed - 'set' object is not callable` | Likely misuse of `.add_edge()` in `graph_builder.py` |
| **Missing API Warnings** | Ensure keys are entered via `.env` or Streamlit sidebar |
| **File Not Found (News)** | Ensure write permissions or manually create `AINews/` folder |

---

## 💬 License & Credits
- Powered by [LangGraph](https://github.com/langchain-ai/langgraph)
- UI built with [Streamlit](https://streamlit.io/)
- Graph-driven agent design using [LangChain](https://www.langchain.com/)
- Special thanks to **Groq** and **Tavily** for their free-tier APIs.

---

## 🙌 Happy Chatting!
Build smarter agents. Learn deeply. Collaborate openly.

Feel free to contribute, raise issues, or suggest new features!


