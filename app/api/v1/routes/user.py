from dependencies import get_database
from peewee import Model
from fastapi import Depends, APIRouter
from app.main import app


router = APIRouter()

@router.post("/signup")
async def signup(username: str, password: str):
    # Your signup logic here
    return {"message": "User signed up successfully"}
