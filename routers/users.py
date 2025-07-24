
from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register_user():
    return {"message": "User registered (placeholder)"}

@router.post("/login")
def login_user():
    return {"message": "User logged in (placeholder)"}
