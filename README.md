# 🤖 AI Support Triage Agent API

A production-style AI Agent API built with FastAPI that classifies, prioritizes, and routes user requests using LLMs, tools, and business logic.

---

## 🚀 Features

- 🧠 AI-powered classification (Bug, Billing, Feature, etc.)
- ⚡ Priority detection (Low, Medium, High)
- 🎯 Confidence scoring
- 🧾 Ticket summary generation
- 🔀 Department routing (Engineering, Finance, Product...)
- 🚨 Escalation logic (rules + AI + tools)
- 🛠 Tool integration:
  - Outage detection
  - Customer lookup (simulated DB)
- 💬 Session-based memory (conversation awareness)
- 📊 Structured logging for observability
- 🧩 Clean modular architecture (services, agents, tools)

---

## 🧱 Architecture

Client → FastAPI → Agent Layer → Tools + LLM → Decision → Response

---

## 📦 Tech Stack

- Python
- FastAPI
- OpenAI API
- Pydantic
- Uvicorn

---

## ⚙️ Setup

1. Clone repo
git clone https://github.com/JawadAyash/ai-agent-api.git

2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Create .env
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4.1-mini

---

## ▶️ Run

uvicorn app.main:app --reload

---

## 🐳 Run with Docker

### Build image

```bash
docker build -t ai-agent-api .
Run container
docker run -p 8000:8000 ai-agent-api

## 👨‍💻 Author

Jawad Ayash
