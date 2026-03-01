from fastapi import APIRouter
from app.schemas.authSchema import Users
from app.controllers import authController
router = APIRouter(
    prefix="/auth", 
    tags=["Auth"]    
)
@router.post("/signup")
def create_user(user: Users):
    return authController.signup(user)
@router.post("/login")
def login_user(user: Users):
    return authController.login(user)
