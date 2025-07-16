# TaskForge Service  
*Lightweight FastAPI microservice for user‑scoped tasks & dynamic JSON templates*

[![Last Commit](https://img.shields.io/github/last-commit/AhmedShaikh-developer/tasktemplate-service?style=flat-square)](https://github.com/AhmedShaikh-developer/tasktemplate-service/commits) [![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)](https://www.python.org/) [![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/) [![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker)](https://www.docker.com/) [![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis)](https://redis.io/)  

---

## Built with  

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com/) [![Uvicorn](https://img.shields.io/badge/Uvicorn-000000?style=flat-square&logo=python)](https://www.uvicorn.org/) [![Pydantic](https://img.shields.io/badge/Pydantic-176EAB?style=flat-square&logo=python)](https://pydantic-docs.helpmanual.io/) [![python‑jose](https://img.shields.io/badge/python--jose-333333?style=flat-square)](https://github.com/mpdavis/python-jose) [![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis)](https://redis.io/) [![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED?style=flat-square&logo=docker)](https://docs.docker.com/compose/)  

---

## 📄 Table of Contents

- [About](#about)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Installation](#installation)  
- [License](#license)  

---

## About

**TaskForge** is a minimal FastAPI application exposing:

1. **User‑Scoped Tasks API** (`/tasks`)  
   - Create, list, and delete simple tasks tied to the authenticated user.  
2. **JSON Templates API** (`/templates`)  
   - Serve a complex multi‑tab JSON form schema and accept filled‑in data.  
3. **JWT Authentication**  
   - Protects all endpoints (except root & docs) using HS256‑signed tokens.  
4. **Pluggable Persistence**  
   - In‑memory prototype by default, with Redis client stub for production.  
5. **Containerized**  
   - Ready to run via Docker & Docker Compose alongside Redis.  

---

## Features

- 🔐 **Secure** endpoints with Bearer JWT (1‑hour expiry).  
- 📋 **Tasks CRUD**: manage your own task list.  
- 📑 **Dynamic Templates**: fetch and submit large JSON schemas.  
- ⚙️ **Configurable** via environment variables.  
- 📦 **Docker‑ready** with Compose integration.  
- 📜 **Auto‑generated docs** at `/docs` (Swagger) and `/redoc`.  

---

## Tech Stack

- **Framework:** FastAPI  
- **Server:** Uvicorn (ASGI)  
- **Auth:** python‑jose (JWT HS256)  
- **Schemas:** Pydantic  
- **Persistence:** Redis (optional) / in‑memory  
- **Containerization:** Docker & Docker Compose  
- **Testing:** pytest & FastAPI TestClient  

---

## Getting Started

### Prerequisites

- Python 3.11+  
- Redis server (optional for production)  
- Docker & Docker Compose (for containerized setup)  

### Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/tasktemplate-service.git
   cd tasktemplate-service

2. **Create & activate virtual environment**  
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt

4. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/tasktemplate-service.git
   cd tasktemplate-service

## Configuration

1. Copy the example environment file and edit secrets:
   ```bash
   cp .env.example .env

2. Open .env and set the following variables:
   ```bash
   SECRET_KEY=your-very-secret-key
   REDIS_HOST=localhost
   REDIS_PORT=6379

3. Usage:
   Running Locally
   Start the FastAPI server with auto‑reload:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000


## Docker & Docker Compose

1. Using Docker Compose- Build and start both app and Redis:
    ```bash
    docker-compose up --build
FastAPI app available at: http://localhost:8000
Redis listening on: localhost:6379

2. Standalone Docker- Build the Docker image:
    ```bash
    docker build -t taskforge-api .
Run the container:
 ```bashdocker run -d \
  -p 8000:8000 \
  --env-file .env \
  --name taskforge-api \
  taskforge-api
