from fastapi import APIRouter

from src.apps.booking.router import router as booking_router


router = APIRouter(prefix="/booking", tags=["booking"])
router.include_router(booking_router)