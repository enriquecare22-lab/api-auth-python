# Auth API - Python Puro + JWT + PostgreSQL

![Python](https://img.shields.io/badge/Python-3.12-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)

Authentication API built with pure Python using the standard `http.server` module and PostgreSQL.

---

# 🚀 Current Features

* User registration endpoint
* PostgreSQL integration
* Password hashing with bcrypt
* Clean Architecture
* Pure Python HTTP Server
* Environment configuration with dotenv

---

# 🧱 Project Structure

```bash
auth-api/
│
├── src/
│   ├── core/
│   ├── domain/
│   ├── application/
│   ├── infrastructure/
│   ├── interfaces/
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Technologies

* Python
* PostgreSQL
* bcrypt
* python-dotenv
* http.server

---

# 📦 Installation

## 1. Clone repository

```bash
git clone <repository-url>
```

---

## 2. Enter project

```bash
cd auth-api
```

---

## 3. Create virtual environment

### Windows

```bash
python -m venv venv
```

---

## 4. Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🌍 Environment Variables

Create `.env`

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=auth_db
DB_USER=postgres
DB_PASSWORD=postgres

JWT_SECRET=supersecretkey
JWT_ALGORITHM=HS256
```

---

# 🗄️ Database

Create PostgreSQL database:

```sql
CREATE DATABASE auth_db;
```

---

# ▶️ Run Project

```bash
python -m src.main
```

---

# 🌐 Current API Endpoints

## Register User

```http
POST /register
```

### Request Body

```json
{
  "email": "test@mail.com",
  "password": "123456"
}
```

---

### Success Response

```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "email": "test@mail.com",
    "role": "user"
  }
}
```

---

# 🔐 Authentication

Authentication and authorization features are currently in development.

---

# 👑 Roles

* user
* admin

