# 🤖 Simple SQL Agent — FastAPI + OpenAI + SQLite

A production-ready AI-powered SQL agent that converts **natural language questions** into safe **SELECT SQL queries**, executes them on SQLite, and returns structured JSON responses—now secured with a dual-proxy architecture.

---

## 🚀 Features

* **Natural Language → SQL:** Powered by OpenAI Responses API.
* **Dual Reverse Proxy:** Simultaneous support for **Traefik v3** and **Caddy 2**.
* **Local SSL/HTTPS:** Encrypted local development using self-signed certificates and Caddy’s internal CA.
* **Security First:** Strict `SELECT`-only execution policy with regex validation.
* **Production-Grade Docker:** Python 3.12 multi-stage builds for a slim, secure image.
* **Health Monitoring:** Automated container health checks and DB connectivity pings.

---

## 🏗 Network & Proxy Architecture

The application is shielded behind two professional-grade reverse proxies, allowing for testing across different environments:

| Service | Protocol | Access URL | Purpose |
| --- | --- | --- | --- |
| **Traefik** | HTTPS | `https://localhost` | Main entry (Port 443) with File Provider TLS. |
| **Caddy** | HTTPS | `https://localhost:8443` | Alternative entry with Automatic Local CA. |
| **SQL Agent** | HTTP | Internal Only | Backend FastAPI service (Port 8000). |
| **Dashboard** | HTTP | `http://localhost:8081` | Traefik Real-time Routing Monitor. |

---

## 🧠 How It Works

1. **Request:** Client hits Traefik or Caddy via HTTPS.
2. **Proxy:** The proxy terminates SSL and forwards the request to the `sql-agent` container.
3. **AI Logic:** FastAPI sends the DB schema + question to OpenAI.
4. **Validation:** Generated SQL is cleaned and verified (must be a `SELECT` statement).
5. **Execution:** The query runs against the persistent SQLite volume.
6. **Response:** Structured JSON is returned back through the proxy.

---

## 🔒 Security & SSL Setup

### Local Certificate Generation

To support Traefik’s local HTTPS, a self-signed certificate is utilized:

```bash
# Generate local keys
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout certs/local.key -out certs/local.crt -subj "/CN=localhost"

```

### Safety Controls

* **Regex-based Validation:** Rejects any query containing `DROP`, `DELETE`, `INSERT`, or `UPDATE`.
* **Isolated Volumes:** Application code (`/app`) is separated from persistent database storage (`/data`).
* **Minimal Exposure:** Only the proxies are exposed to the host; the app remains private on the Docker network.

---

## 📦 Getting Started

1. **Configure Environment:** Add your `OPENAI_API_KEY` to the `.env` file.
2. **Generate Certs:** Run the openssl command above.
3. **Launch:**
```bash
docker compose up --build -d

```



**API Documentation:** `https://localhost/docs`

**Health Status:** `https://localhost/health`

---

## 🎯 Project Vision

This setup provides a high-security foundation for AI-powered analytics, demonstrating how to bridge LLM capabilities with hardened DevOps practices like reverse proxying, SSL termination, and container orchestration.

---