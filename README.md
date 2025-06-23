# 📝 NoteTakingApp

A full-stack note-taking application built with **React (Frontend)** and **Flask + SQLAlchemy (Backend)**, deployed on **Render** using **GitHub Actions CI/CD**.

<br/>

## 🔗 Live Demo

- **Frontend**: [https://note-frontend-9vcp.onrender.com](https://note-frontend-9vcp.onrender.com)
- **Backend**: [https://note-backend-bajx.onrender.com](https://note-backend-bajx.onrender.com)

> ⚠️ The backend may take 30–50 seconds to wake up on Render free tier.

---

## 🏗️ Tech Stack

| Layer     | Technology               |
|-----------|---------------------------|
| Frontend  | React, Axios, Lodash     |
| Backend   | Flask, SQLAlchemy, CORS  |
| Database  | SQLite                   |
| CI/CD     | GitHub Actions           |
| Hosting   | Render (Docker-based)    |

---

## 📁 Folder Structure

```
NoteTakingApp/
│
├── .github/workflows/        # CI/CD pipeline
├── backend/                  # Flask API + DB models
│   ├── models/
│   ├── routes/
│   ├── extensions.py
│   └── app.py
│
├── src/                      # React frontend source
│   ├── Components/
│   ├── App.js
│   ├── index.js
│   └── api.js                # BASE_URL config
│
├── Dockerfile                # Multi-stage React build
├── docker-compose.yml        # For dev environment
├── .dockerignore
└── README.md                 # This file
```

---

## ⚙️ Local Development

### 🔧 Backend (Flask)

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux

pip install -r requirements.txt
flask run
```

### 💻 Frontend (React)

```bash
cd src
npm install
npm start
```

---

## 🚀 Deployment (CI/CD with GitHub Actions)

Every push to the `main` branch automatically triggers deployment via Render:

```yaml
name: Deploy to Render

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Trigger Render Deploy (Backend)
        run: |
          curl -X POST "https://api.render.com/deploy/srv-d1cp1lmmcj7s73b71ld0?key=${{ secrets.RENDER_API_KEY }}"

      - name: Trigger Render Deploy (Frontend)
        run: |
          curl -X POST "https://api.render.com/deploy/srv-d1cop3mmcj7s73b6og7g?key=${{ secrets.RENDER_API_KEY }}"
```

---

## 🎯 Future Improvements

- Add user authentication (JWT)
- Migrate to PostgreSQL for production database
- Enable persistent disk or cloud storage (e.g., AWS S3)
- Add features like tagging, rich text editing, and pinning notes
