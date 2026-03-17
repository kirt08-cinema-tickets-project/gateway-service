from fastapi import APIRouter

from src.apps.screening.router import router as screening_router


router = APIRouter(prefix="/screening", tags=["screening"])
router.include_router(screening_router)