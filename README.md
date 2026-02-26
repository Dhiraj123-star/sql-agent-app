# 🤖 Simple SQL Agent — FastAPI + OpenAI + SQLite

A production-ready AI-powered SQL agent that converts **natural language questions** into safe **SELECT SQL queries**, executes them on SQLite, and returns structured JSON responses.

---

## 🚀 Features

* Natural language → SQL generation
* Powered by **OpenAI Responses API**
* Strict `SELECT`-only execution policy
* Automatic SQL cleaning & validation
* Structured JSON responses
* `/health` endpoint with DB connectivity check
* Dockerized with **Python 3.12 (multi-stage build)**
* Clean container architecture (`/app` + `/data`)
* Persistent SQLite storage via mounted volume

---

## 🧠 How It Works

1. Client sends a question to `/query`
2. App provides DB schema + question to OpenAI
3. OpenAI generates SQL
4. SQL is cleaned and validated
5. Only safe `SELECT` queries are executed
6. Results returned in structured JSON format

---

## 🏗 Container Architecture

```
Container
│
├── /app   → Application code
└── /data  → SQLite database file
```

* Code and data are isolated
* No volume overrides
* Clean production-ready layout

---

## 🛠 Tech Stack

* **FastAPI** – API framework
* **OpenAI Responses API** – LLM reasoning
* **SQLite** – Embedded database
* **SQLAlchemy** – Database engine/session handling
* **Pydantic** – Data validation
* **Docker + Docker Compose** – Containerization
* **Uvicorn** – ASGI server

---

## 🔒 Safety Controls

* Regex-based SQL validation
* Rejects non-`SELECT` queries
* No schema modification allowed
* Limited schema exposure to LLM
* Health monitoring via `/health`

---

## 📦 Run with Docker

```bash
docker compose up --build
```

API Docs:

```
http://localhost:8000/docs
```

Health Check:

```
http://localhost:8000/health
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
  "result": [
    { "COUNT(*)": 2 }
  ]
}
```

---

## 🎯 Project Vision

This project serves as a foundation for:

* AI-powered database copilots
* Internal analytics assistants
* Secure natural language data querying systems
* LLM-driven backend microservices

---