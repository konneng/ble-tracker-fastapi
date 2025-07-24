
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_tags():
    return {"tags": []}

@router.post("/")
def add_tag():
    return {"message": "New tag added (placeholder)"}
