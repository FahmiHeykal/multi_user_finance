# Multi-User Finance Tracker API

A simple, clean, and secure RESTful API for tracking income and expense transactions per user. Built using FastAPI and PostgreSQL, this project supports multi-user authentication, transaction logging, and CSV export.

---

## Features

- User registration and login using JWT
- Secure password hashing with bcrypt
- Create, read, update, delete (CRUD) financial transactions
- Export user transactions to CSV
- Data access restricted to logged-in users only

---

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Passlib (bcrypt)
- Python-JOSE (JWT)
- Uvicorn

---

## Project Structure
multi_user_finance/
├── app/
│ ├── api/
│ │ └── routes/
│ ├── db/
│ ├── models/
│ ├── schemas/
│ └── main.py
├── .env
├── requirements.txt
└── README.md



---

## Setup Instructions

1. **Clone the Repository**

   git clone https://github.com/yourusername/multi_user_finance.git  
   cd multi_user_finance

2. **Install Dependencies**

   pip install -r requirements.txt

3. **Create a `.env` File**

   Fill in the following environment variables:

   - `DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/finance_db`
   - `SECRET_KEY=your_secret_key`
   - `ALGORITHM=HS256`
   - `ACCESS_TOKEN_EXPIRE_MINUTES=60`

4. **Create the PostgreSQL Database**

   Create a new database named `finance_db` manually or using a tool like pgAdmin.

5. **Run the Server**

   uvicorn app.main:app --reload

---

## API Usage (via Postman or any HTTP client)

### 1. Register

- Endpoint: `POST /auth/register`
- Body:
  - `username`: your desired username
  - `password`: your desired password

### 2. Login

- Endpoint: `POST /auth/login`
- Body:
  - `username`: your username
  - `password`: your password
- Response:
  - `access_token`: used to authorize requests

### 3. Add a Transaction

- Endpoint: `POST /transactions/`
- Headers:
  - `Authorization: Bearer <access_token>`
- Body:
  - `amount`: nominal amount (e.g. 100000)
  - `description`: short description (e.g. Gaji)

### 4. Export Transactions

- Endpoint: `GET /export/`
- Headers:
  - `Authorization: Bearer <access_token>`

This will download all your transactions as a CSV file.

---

## Planned Features

- Transaction categories (income, expense types)
- Weekly and monthly summaries
- User profile endpoint
- Admin role support
- Graphs or analytics endpoint
