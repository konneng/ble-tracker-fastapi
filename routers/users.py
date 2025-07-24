
from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register():
    return {"msg": "User registration placeholder"}

@router.post("/login")
def login():
    return {"msg": "User login placeholder"}
