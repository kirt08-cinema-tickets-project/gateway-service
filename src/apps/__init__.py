from fastapi import APIRouter

from src.apps.auth.router import router as auth_router

router = APIRouter()

router.include_router(auth_router)
