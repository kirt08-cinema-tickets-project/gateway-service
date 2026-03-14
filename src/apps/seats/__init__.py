from fastapi import APIRouter

from src.apps.seats.router import router as seats_router


router = APIRouter(prefix="/seats", tags=["seats"])
router.include_router(seats_router)