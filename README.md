
# 🤖 Simple SQL Agent — FastAPI + OpenAI + SQLite

A lightweight AI-powered SQL agent that converts **natural language questions** into safe **SELECT SQL queries**, executes them on SQLite, and returns structured JSON results.

---

## 🚀 Features

* Convert natural language → SQL
* Uses **OpenAI Responses API**
* Executes dynamically generated SQL
* Strictly allows only `SELECT` queries
* Returns structured JSON responses
* Dockerized (Python 3.12, multi-stage build)
* SQLite persistence via Docker volume

---

## 🧠 How It Works

1. Client sends a question to `/query`
2. Agent receives database schema + user question
3. OpenAI generates SQL
4. SQL is validated (only `SELECT` allowed)
5. Query executes on SQLite
6. Results returned as JSON

---

## 🛠 Tech Stack

* **FastAPI** – API framework
* **OpenAI Responses API** – LLM reasoning
* **SQLite** – Local database
* **SQLAlchemy** – Database interaction
* **Pydantic** – Data validation
* **Docker + Docker Compose** – Containerization (Python 3.12)

---

## 🔒 Safety Controls

* Regex-based SQL validation
* Rejects non-`SELECT` queries
* No schema modification allowed
* Controlled database exposure

---

## 📦 Run with Docker

```bash
docker compose up --build
```

API Docs:

```
http://localhost:8000/docs
```

---

## 📌 Example

### Request

```json
POST /query
{
  "question": "How many admin users are there?"
}
```

### Response

```json
{
  "sql": "SELECT COUNT(*) FROM users WHERE role='admin';",
  "result": [[2]]
}
```

---

## 🎯 Project Vision

This project serves as a foundation for:

* AI-powered database copilots
* Internal analytics assistants
* Natural language data querying systems
* Secure LLM-driven backend services

---

