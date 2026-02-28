__all__ = [
    "router"
]

from fastapi import APIRouter

from src.apps.users.router import router as users_router

router = APIRouter(prefix="/users", tags=["users"])
router.include_router(users_router)