from app.db.authDb import user_collection
from app.schemas.authSchema import Users
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
import hashlib

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


def signup(user: Users):
    existing_user = user_collection.find_one({"email": user.email})
    if existing_user:
        return {"message": "User already exists"}
    hashed_password = hash_password(user.password)

    user_data = {
        "email": user.email,
        "password": hashed_password,
    }

    user_collection.insert_one(user_data)

    return {"message": "User created successfully"}


def login(user: Users):
    db_user = user_collection.find_one({"email": user.email})
    if not db_user:
        return {"message": "User not found"}
    if not verify_password(user.password, db_user["password"]):
        return {"message": "Invalid password"}
    token = create_access_token(
        {"email": db_user["email"], "user_id": str(db_user["_id"])}
    )
    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer",
        "user": {"id": str(db_user["_id"]), "email": db_user["email"]},
    }
