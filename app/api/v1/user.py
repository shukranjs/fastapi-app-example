from dependencies import get_database
from peewee import Model
from fastapi import Depends
from app.main import app


@app.get("/")
async def read_root(db: Model = Depends(get_database)):
    return {"message": "Hello, FastAPI!"}
