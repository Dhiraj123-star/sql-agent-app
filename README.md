# 🤖 Simple SQL Agent — FastAPI + OpenAI + SQLite

A minimal AI-powered SQL agent that converts **natural language questions** into safe **SELECT SQL queries**, executes them on a local SQLite database, and returns structured results.

---

## 🚀 What This Project Does

* Accepts natural language questions via API
* Uses **OpenAI Responses API**
* Generates SQL dynamically
* Executes only safe `SELECT` queries
* Returns query results in JSON
* Uses a local SQLite database

---

## 🧠 How It Works

1. User sends a question (`/query`)
2. Agent receives DB schema + question
3. Agent generates SQL
4. App validates SQL (only `SELECT`)
5. SQL runs against SQLite
6. Results are returned

---

## 🛠 Tech Stack

* **FastAPI** – API framework
* **OpenAI Responses API** – LLM reasoning
* **SQLite** – Local database
* **SQLAlchemy** – ORM
* **Pydantic** – Request/response validation

---

## 🔒 Safety Features

* Only `SELECT` queries allowed
* Basic SQL validation layer
* Controlled schema exposure
* No destructive DB operations

---

## 📌 Example Request

```json
POST /query
{
  "question": "How many admin users are there?"
}
```

### Example Response

```json
{
  "sql": "SELECT COUNT(*) FROM users WHERE role='admin';",
  "result": [[2]]
}
```

---

## 🎯 Project Goal

A simple foundation for building:

* AI-powered database assistants
* Internal analytics copilots
* Natural language data interfaces

---


