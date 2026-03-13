<div align="center">

# 🤖 Monday Business Intelligence AI Agent

### Conversational Analytics · Monday.com Integration · LLM-Powered Insights

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask)
![Monday.com](https://img.shields.io/badge/Monday.com-GraphQL%20API-FF3D57?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-AI%20Model-F55036?style=for-the-badge)
![Render](https://img.shields.io/badge/Deployed-Render-46E3B7?style=for-the-badge&logo=render)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

An AI-powered conversational analytics assistant that connects with **Monday.com Work Order Tracker**, processes business data, and delivers real-time insights using Large Language Models.

Instead of manually analyzing dashboards or spreadsheets — users simply **ask questions in plain English**.

🚀 **[Live Demo →](https://agentic-chatbot-4g8y.onrender.com)**

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Application Flow](#-application-flow)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Deployment](#-deployment-render)
- [Monday.com Integration](#-mondaycom-integration)
- [AI Integration](#-ai-integration)
- [Example Questions](#-example-user-questions)
- [Security Decisions](#-security-decisions)
- [Error Handling](#-error-handling)
- [Design Decisions](#-design-decisions)
- [Future Improvements](#-future-improvements)

---

## 🔷 Overview

> The **Monday Business Intelligence AI Agent** allows business users to ask natural language questions about project performance, billing status, revenue trends, and operational insights — powered by Monday.com data and LLM-generated analysis.

| Capability | Implementation |
|---|---|
| Data Source | Monday.com GraphQL API |
| AI Layer | Groq / OpenAI LLM |
| Interface | Conversational Chat UI |
| Backend | Flask + Gunicorn |
| Deployment | Render (Cloud) |

---

## ✨ Key Features

```
✅ Conversational analytics interface
✅ Monday.com API integration (GraphQL)
✅ AI-generated business insights
✅ Structured revenue summaries
✅ Billing and project tracking insights
✅ Cloud deployed on Render
✅ Secure environment variable handling
✅ Graceful error-handled API integration
```

---

## 🏗 System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    USER INTERFACE                            │
│              HTML + CSS + JavaScript                         │
└──────────────────────────┬───────────────────────────────────┘
                           │
                           │  POST /ask
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                   FLASK BACKEND API                          │
│  • Receives natural language questions                       │
│  • Orchestrates data fetch + AI call                         │
│  • Returns structured AI response                            │
└──────────────┬───────────────────────────┬───────────────────┘
               │                           │
               ▼                           ▼
┌──────────────────────┐     ┌─────────────────────────────────┐
│   MONDAY.COM API     │     │        AI MODEL LAYER           │
│   (GraphQL)          │     │        (Groq / OpenAI)          │
│                      │     │                                 │
│  • Work Order Boards │     │  • Prompt Engineering           │
│  • Project Data      │     │  • Insight Generation           │
│  • Billing Status    │     │  • Conversational Responses     │
└──────────────────────┘     └─────────────────────────────────┘
```

---

## 🔁 Application Flow

```
User asks a natural language question
            │
            ▼
Frontend sends POST request → /ask
            │
            ▼
Flask Backend receives question
            │
            ├──▶  Fetch Monday.com board data (GraphQL)
            │
            ├──▶  Clean + Structure data
            │
            └──▶  Send structured data + prompt to AI model
                            │
                            ▼
                  AI generates business insights
                            │
                            ▼
                  Response returned to chat UI
```

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Flask + Gunicorn |
| **AI Model** | Groq / OpenAI |
| **Data Source** | Monday.com GraphQL API |
| **Deployment** | Render |
| **Language** | Python 3.10+ |

---

## 📂 Project Structure

```
monday-ai-agent/
│
├── app.py                  # Flask application & route handlers
├── chatbot.py              # AI logic & prompt engineering
├── monday_client.py        # Monday.com API integration
│
├── templates/
│   └── index.html          # Conversational chat UI
│
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed)
├── .gitignore
└── README.md
```

---

## ⚙ Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd monday-ai-agent
```

**2. Create and activate virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Create a `.env` file in the project root:

```env
MONDAY_API_KEY=your_monday_api_key
GROQ_API_KEY=your_groq_api_key
```

**5. Run locally**

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment (Render)

**Build command:**

```bash
pip install -r requirements.txt
```

**Start command:**

```bash
gunicorn app:app
```

**Environment variables to set in Render dashboard:**

```
MONDAY_API_KEY
GROQ_API_KEY
```

---

## 🔌 Monday.com Integration

The application connects to a Monday.com Work Order Tracker board using GraphQL queries.

**Example query:**

```graphql
query {
    boards(ids: BOARD_ID) {
        items_page(limit: 50) {
            items {
                name
                column_values {
                    text
                    column {
                        title
                    }
                }
            }
        }
    }
}
```

Data retrieved includes project names, billing status, revenue figures, and operational status per work order.

---

## 🤖 AI Integration

The LLM layer is used to:

```
✔  Analyze business performance from structured board data
✔  Summarize revenue trends and billing status
✔  Answer conversational queries in plain English
✔  Generate structured, actionable business responses
```

---

## 🧾 Example User Questions

```
"How many completed projects?"
"Which projects are partially billed?"
"What are the major revenue drivers?"
"Show all ongoing projects."
"Which sector generates the highest revenue?"
```

---

## 🛡 Security Decisions

```
✅ API keys stored exclusively in environment variables
✅ .env file excluded via .gitignore
✅ No sensitive data committed to GitHub
✅ Keys injected at runtime via Render environment config
```

---

## ⚠ Error Handling

The application gracefully handles API failures, missing fields, and model errors:

```python
try:
    answer = ask_question(question)
except Exception as e:
    return jsonify({"answer": str(e)})
```

Errors handled:

```
→ Invalid or expired API keys
→ Missing or malformed data fields
→ Monday.com API failures or rate limits
→ AI model timeouts or response errors
```

---

## 📊 Design Decisions

| Decision | Rationale |
|---|---|
| Flask Backend | Lightweight, fast API development with minimal overhead |
| Monday GraphQL API | Flexible, structured data retrieval per query |
| AI Insight Layer | Natural language interface replaces manual dashboard analysis |
| Render Deployment | Simple CI/CD pipeline with built-in environment variable management |
| Gunicorn Server | Production-grade WSGI server for reliability |

---

## 🚀 Future Improvements

```
[ ] Dashboard visualizations with charts
[ ] User authentication and login
[ ] Role-based access control (RBAC)
[ ] Caching AI responses to reduce API calls
[ ] Streaming real-time AI responses
[ ] Multi-board aggregation and cross-project analytics
[ ] Chart-based insights rendered in the UI
```

---

## 👨‍💻 Author

**Shreyas Dewang Swami**

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with Flask · Monday.com API · Groq · Render**

⭐ Star this repo if you found it helpful!

</div>
