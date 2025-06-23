# 🗒️ NoteTakingApp

A full-stack note-taking web application built using React (frontend) and Flask (backend). The project supports creating, updating, and deleting notes — all fully containerized using Docker and orchestrated via Docker Compose.

---

## 📦 Features

- 🖍️ Add colorful notes
- 🗑️ Delete notes
- ✏️ Auto-save notes with debounce
- 🔗 Fully connected frontend and backend via REST API
- 🐳 Dockerized frontend & backend
- 📦 One-command startup with Docker Compose

---

## 🧾 Tech Stack

- **Frontend**: React, Axios, Lodash
- **Backend**: Flask, Flask-CORS, SQLAlchemy
- **Database**: SQLite
- **Containerization**: Docker
- **Dev Orchestration**: Docker Compose

---

### 🛠 Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your machine

---

### ▶️ Run the App

```bash
# Step into the project directory
cd NoteTakingApp

# Start both frontend and backend
docker-compose up --build

Now visit: http://localhost:3000
