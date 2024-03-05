from fastapi import Depends, APIRouter
from app.models.user import User
from app.dependecies import get_database
from app.schemas.user import UserCreate
from app.database import MySQLDatabase

router = APIRouter()


@router.post("/signup")
async def signup(
    user_data: UserCreate, database: MySQLDatabase = Depends(get_database)
):
    if User.select().where(User.username == user_data.username).exists():
        return {"message": "Username already exists"}
    if User.select().where(User.email == user_data.email).exists():
        return {"message": "Email already exists"}

    new_user = User.create(
        username=user_data.username,
        email=user_data.email,
        password=user_data.password,
        database=database,
    )
    return {"message": "User signed up successfully", "user_id": new_user.id}


@router.get("/users")
async def list_users():
    users = User.select()
    user_list = [{"username": user.username, "email": user.email} for user in users]
    return {"users": user_list}
