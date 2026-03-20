from fastapi import APIRouter

from src.apps.refund.router import router as refund_router


router = APIRouter(prefix="/refund", tags=["refund"])
router.include_router(refund_router)