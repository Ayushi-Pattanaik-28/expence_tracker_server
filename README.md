# 💰 Personal Expense & Income Tracker – Backend

Backend API for the Personal Expense & Income Tracker assignment.

Built with:

- FastAPI
- MongoDB
- PyMongo
- JWT Authentication
- Passlib (bcrypt password hashing)

---

## 🚀 Features

- User Registration
- User Login
- JWT Token Generation
- Secure Protected Routes
- User-specific Transactions
- Add Income / Expense
- Update Transaction (Owner Protected)
- Delete Transaction (Owner Protected)
- Get All Transactions

---
---

## 📂 Folder Structure

app/
│
├── controllers/
│ ├── authController.py
│ └── expenseController.py
│
├── db/
│ ├── authDb.py
│ └── expenseDb.py
│
├── middlewares/
│ └── authMiddleware.py
│
├── routes/
│ ├── authRoutes.py
│ └── expenseRoutes.py
│
├── schemas/
│ ├── authSchema.py
│ └── expenseSchema.py
│
└── main.py

---

## ⚙️ Setup Instructions

### 1️⃣ Clone repository

```bash
git clone <backend-repo-url>
cd backend

2️⃣ Create virtual environment
python -m venv venv

Activate:

Windows
venv\Scripts\activate

Mac/Linux
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run server
uvicorn app.main:app --reload

Server runs at:
http://127.0.0.1:8000

Swagger Docs:
http://127.0.0.1:8000/docs

🔐 Authentication
JWT-based authentication
Passwords hashed using bcrypt
Protected routes use HTTPBearer

Token contains:
user_id
email
Token expiry: 60 minutes
Protected routes require:
Authorization: Bearer <token>

🗄 Database
MongoDB collections:
users
expenses
Each expense is linked using:
user_id

📌 API Endpoints
Auth
POST /auth/signup
POST /auth/login
Expenses
GET /expense/
POST /expense/
PUT /expense/{id}
DELETE /expense/{id}

🛡 Security
No plain-text passwords
JWT verification on every protected route
User ownership validation on update/delete

