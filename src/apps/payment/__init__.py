from fastapi import APIRouter

from src.apps.payment.router import router as payment_router


router = APIRouter(prefix="/payment", tags=["payment"])
router.include_router(payment_router)