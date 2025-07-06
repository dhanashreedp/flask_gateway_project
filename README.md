# 🔗 API Gateway with Django Microservices and Streamlit UI

This project showcases a microservices architecture using **Django** for backend services (Authentication, Analytics, Data Processing), a **Flask API Gateway** to orchestrate service communication, and a **Streamlit UI** to interact with users.

---

## 📌 Overview

- 🔐 **Auth Service** → Register/Login APIs (Django)
- 📊 **Analytics Service** → Event tracking APIs (Django)
- 🧠 **Data Service** → Text processing APIs (Django)
- 🚪 **API Gateway** → Routes all external requests (Flask)
- 🌐 **UI** → Simple UI to consume services (Streamlit)

---

## 🏗 Architecture

```text
+------------------+
|   Streamlit UI   |
+--------+---------+
         |
         v
+--------+---------+        (http://localhost:5000)
|  Flask API Gateway |
+--------+---------+
         |
  -------------------------------
  |           |                |
  v           v                v
 Auth     Analytics       Data Service
(Django)   (Django)          (Django)
:8000       :8001             :8002
````

---

## 🗂 Project Structure

```text
flask_gateway_project/
├── auth_service/               # Django Authentication Service (:8000)
│   ├── auth_service/           # Django project (settings, urls)
│   ├── accounts/               # Register/Login logic
│   └── manage.py
├── analytics_service/          # Django Analytics Service (:8001)
│   ├── analytics_service/
│   ├── core/                   # Event tracking
│   └── manage.py
├── data_service/               # Django Data Processing Service (:8002)
│   ├── data_service/
│   ├── processor/              # Text summarization
│   └── manage.py
├── api_gateway/
│   ├── app.py                  # Flask API Gateway
│   └── routes/                 # Modular blueprints
├── ui_app.py                   # Streamlit UI
├── requirements.txt            # Shared dependencies
└── venv/                       # Virtual Environment (optional)
```

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

* Python 3.8+
* pip
* Git
* Virtualenv

---

### 🛠 Installation

🔹 Clone and Setup Project</strong></summary>

```bash
git clone https://github.com/YOUR_USERNAME/flask_gateway_project.git
cd flask_gateway_project
```

🔹 Set Up Virtual Environments</strong></summary>

* **Main venv** for Flask Gateway + Streamlit:

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
deactivate
```

* **Each Django service (repeat per service)**

```bash
cd auth_service
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
deactivate
```
Repeat for `analytics_service/` and `data_service/`.
---

## 🚀 Running the Project

Run each service in its own terminal:

### 🟩 1. Auth Service

```bash
cd auth_service
.\venv\Scripts\activate
python manage.py runserver 8000
```

### 🟨 2. Analytics Service

```bash
cd analytics_service
.\venv\Scripts\activate
python manage.py runserver 8001
```

### 🟦 3. Data Service

```bash
cd data_service
.\venv\Scripts\activate
python manage.py runserver 8002
```

### 🔵 4. Flask API Gateway

```bash
cd api_gateway
.\venv\Scripts\activate
python app.py  # runs on http://localhost:5000
```

### 🟣 5. Streamlit UI

```bash
cd flask_gateway_project
.\venv\Scripts\activate
streamlit run ui_app.py
```

---

## 🌐 Try Endpoints (Optional)

Test services manually using:
* Postman / Curl
* Or visit:

```
http://localhost:8000/api/register/
http://localhost:8001/api/track/
http://localhost:8002/api/process/
```

---

## 📌 Future Enhancements

* ✅ Dockerize each service
* 🔐 JWT Authentication across all services
* 📊 Add database dashboard
* ☁️ Deploy to Render / Streamlit Cloud

---

## 📄 License

MIT License © 2025 Dhanashree Patil

---

## 🙋‍♀️ Author

**Dhanashree Patil**
🔗 [LinkedIn](https://www.linkedin.com/in/dhanashree-patil)
💻 [GitHub](https://github.com/dhanashree-patil)

---

