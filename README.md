

# 🤖 Monday Business Intelligence AI Agent

An AI-powered conversational analytics assistant that connects with **Monday.com Work Order Tracker**, processes business data, and delivers real-time insights using Large Language Models.

---

## 🚀 Live Demo

👉 https://agentic-chatbot-4g8y.onrender.com

---

## 📌 Overview

The **Monday Business Intelligence AI Agent** allows business users to ask natural language questions about project performance, billing status, revenue trends, and operational insights.

Instead of manually analyzing dashboards or spreadsheets, users interact with a conversational AI interface.

---

## 🧠 Key Features

* Conversational analytics interface
* Monday.com API integration
* AI-generated business insights
* Structured revenue summaries
* Billing and project tracking insights
* Cloud deployed application
* Secure environment variable handling
* Error-handled API integration

---

## 🏗️ Architecture Overview

```
User Interface (HTML + JS)
          │
          ▼
Flask Backend API
          │
          ├── Monday.com API
          │       (Business Data Source)
          │
          └── AI Model (Groq/OpenAI)
                  (Insight Generation)
```

---

## 🔄 Application Flow

```
User Question
     │
     ▼
Frontend sends POST request → /ask
     │
     ▼
Flask Backend receives question
     │
     ├── Fetch Monday board data
     │
     ├── Clean + Structure Data
     │
     └── Send structured data + prompt to AI model
                │
                ▼
         AI generates insights
                │
                ▼
         Response returned to UI
```

---

## 🛠️ Tech Stack

| Layer       | Technology             |
| ----------- | ---------------------- |
| Frontend    | HTML, CSS, JavaScript  |
| Backend     | Flask                  |
| AI Model    | Groq / OpenAI          |
| Data Source | Monday.com GraphQL API |
| Deployment  | Render                 |
| Server      | Gunicorn               |

---

## 📁 Project Structure

```
monday-ai-agent/
│
├── app.py                # Flask application
├── chatbot.py            # AI logic & prompt engineering
├── monday_client.py      # Monday API integration
├── templates/
│      └── index.html     # Chat UI
├── requirements.txt      # Dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd monday-ai-agent
```

---

### 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create `.env` file:

```
MONDAY_API_KEY=your_monday_api_key
GROQ_API_KEY=your_groq_api_key
```

---

### 5️⃣ Run Locally

```bash
python app.py
```

Application will run on:

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment (Render)

### Build Command

```
pip install -r requirements.txt
```

### Start Command

```
gunicorn app:app
```

### Environment Variables (Render Dashboard)

```
MONDAY_API_KEY
GROQ_API_KEY
```

---

## 🔌 Monday.com Integration

The application connects to Monday Work Order Tracker using GraphQL queries.

Example:

```python
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

---

## 🤖 AI Integration

AI models are used to:

* Analyze business performance
* Summarize revenue insights
* Answer conversational queries
* Generate structured responses

---

## 🧾 Example User Questions

```
How many completed projects?
Which projects are partially billed?
What are the major revenue drivers?
Show ongoing projects.
Which sector generates highest revenue?
```

---

## 🛡️ Security Decisions

* API keys stored in environment variables
* `.env` excluded via `.gitignore`
* No sensitive data committed to GitHub

---

## ⚠️ Error Handling

The application gracefully handles:

* Invalid API keys
* Missing data fields
* Monday API failures
* AI model errors

Example:

```python
try:
    answer = ask_question(question)
except Exception as e:
    return jsonify({"answer": str(e)})
```

---

## 📊 Design Decisions

| Decision          | Reason                                 |
| ----------------- | -------------------------------------- |
| Flask Backend     | Lightweight & fast API development     |
| Monday GraphQL    | Flexible structured data retrieval     |
| AI Insight Layer  | Natural language business intelligence |
| Render Deployment | Simple CI/CD & hosting                 |

---

## 🔮 Future Improvements

* Dashboard visualizations
* User authentication
* Role-based access
* Caching AI responses
* Streaming responses
* Multi-board analytics
* Chart-based insights

---

## 👨‍💻 Author

**Shreyas Dewang Swami**

---

## ⭐ License

MIT License

---

---

# 📌 Assignment Reflection

### What I Would Improve With More Time

* Add visual analytics dashboard
* Implement authentication
* Improve multi-board aggregation
* Add real-time streaming insights

---

### Leadership Updates Interpretation

The agent prioritizes:

* Revenue clarity
* Risk identification
* Billing transparency
* Project performance summarization
