# 🚀 API Gateway with Django Microservices and Streamlit UI

This project demonstrates a microservices architecture using **Django** for backend services (Authentication, Analytics, Data Processing), a **Flask** API Gateway, and a **Streamlit** UI for easy interaction.

---

## 📚 Table of Contents

- [💡 Introduction](#-introduction)
- [🏗 Architecture Overview](#-architecture-overview)
- [🗂 Project Structure](#-project-structure)
- [⚙️ Setup & Running Locally](#️-setup--running-locally)
  - [🔧 Prerequisites](#-prerequisites)
  - [📦 Clone the Repository](#-clone-the-repository)
  - [🐍 Virtual Environments](#-virtual-environments)
  - [📥 Install Dependencies](#-install-dependencies)
  - [🧱 Database Migrations](#-database-migrations)
  - [▶️ Running the Services](#-running-the-services)
- [🌐 Deployment to GitHub](#-deployment-to-github)
- [✨ Future Enhancements](#-future-enhancements)
- [🪪 License](#-license)

---

## 💡 Introduction

This repository contains a modular microservices-based setup:

- 🧑‍💼 **Authentication Service** (Django): Handles user registration/login  
- 📊 **Analytics Service** (Django): Tracks user events  
- ⚙️ **Data Processing Service** (Django): Text transformation APIs  
- 🔀 **Flask API Gateway**: Routes and unifies communication  
- 🧑‍🎤 **Streamlit UI**: Web frontend to access services

---

## 🏗 Architecture Overview

           ┌──────────────────────┐
           │     Streamlit UI     │
           │ http://localhost:8501│
           └─────────┬────────────┘
                     │
             (Requests via Port 5000)
                     ▼
           ┌──────────────────────┐
           │   Flask API Gateway  │
           │ http://localhost:5000│
           └─────────┬────────────┘
        ┌────────────┼────────────┬────────────┐
        ▼            ▼            ▼
    ┌────────────┐ ┌────────────┐ ┌────────────┐
    │ Auth       │ │ Analytics  │ │ Data       │
    │ Service    │ │ Service    │ │ Service    │
    │ :8000      │ │ :8001      │ │ :8002      │
    └────────────┘ └────────────┘ └────────────┘

🗂 Project Structure

flask_gateway_project/
├── auth_service/          # Django Authentication Service
│   ├── accounts/          # Auth app: register/login
│   ├── auth_service/      # Django project settings
│   └── manage.py
├── analytics_service/     # Django Analytics Service
│   └── core/              # Analytics logic
├── data_service/          # Django Data Processing Service
│   └── processor/         # Text processing APIs
├── api_gateway/
│   ├── app.py             # Flask API Gateway
│   └── routes/            # Modular blueprints
├── ui_app.py              # Streamlit UI
├── requirements.txt       # Global or shared requirements
└── venv/                  # (Optional) Virtual Environment

⚙️ Setup & Running Locally

🔧 Prerequisites

Python 3.8+
pip

📦 Clone the Repository
git clone https://github.com/your-username/flask_gateway_project.git
cd flask_gateway_project

🐍 Virtual Environments
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux
Repeat for each Django microservice (auth, analytics, data)

📥 Install Dependencies
Create individual requirements.txt in each service.
Example for auth_service/requirements.txt:
Django==5.2.4
djangorestframework
django-extensions

Install like so:
cd auth_service
.\venv\Scripts\activate
pip install -r requirements.txt
deactivate

Repeat for each service and for Flask/Streamlit:
pip install flask flask-cors requests streamlit

🧱 Database Migrations
For each Django service:
cd auth_service
.\venv\Scripts\activate
python manage.py makemigrations
python manage.py migrate
deactivate

▶️ Running the Services
Start each service in separate terminals:
# Auth Service (port 8000)
cd auth_service
.\venv\Scripts\activate
python manage.py runserver 8000

# Analytics Service (port 8001)
cd analytics_service
.\venv\Scripts\activate
python manage.py runserver 8001

# Data Service (port 8002)
cd data_service
.\venv\Scripts\activate
python manage.py runserver 8002

# API Gateway (port 5000)
cd api_gateway
.\venv\Scripts\activate
python app.py

# Streamlit UI (port 8501)
cd flask_gateway_project
streamlit run ui_app.py

✨ Future Enhancements
Add JWT-based authentication
Dockerize microservices
Switch to PostgreSQL
Deploy on AWS/GCP/Azure

🪪 License
MIT License © 2025 Dhanashree Patil

