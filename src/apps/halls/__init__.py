from fastapi import APIRouter

from src.apps.halls.router import router as halls_router


router = APIRouter(prefix="/halls", tags=["halls"])
router.include_router(halls_router)