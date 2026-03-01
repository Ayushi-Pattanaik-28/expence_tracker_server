from pydantic import BaseModel, EmailStr, Field


class Users(BaseModel):
    email: EmailStr

    password: str = Field(..., min_length=7)