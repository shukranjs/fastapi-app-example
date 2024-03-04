from fastapi import APIRouter

from app.api.v1.routes import task, user

router = APIRouter()

router.include_router(router=user.router, tags=["User"], prefix="/users")
router.include_router(router=task.router, tags=["Tasks"], prefix="/tasks")
