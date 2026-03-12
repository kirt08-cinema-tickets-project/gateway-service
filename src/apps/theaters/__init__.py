__all__ = [
    "router"
]

from fastapi import APIRouter

from src.apps.theaters.router import router as theaters_router

router = APIRouter(prefix="/theaters", tags=["theaters"])
router.include_router(theaters_router)