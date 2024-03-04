from peewee import Model
from fastapi import Depends, APIRouter
from app.main import app
from app.dependecies import get_database

router = APIRouter()

@router.post("/signup")
async def signup(username: str, password: str):
    return {"message": "User signed up successfully"}
