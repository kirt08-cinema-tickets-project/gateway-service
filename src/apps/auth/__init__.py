from fastapi import APIRouter

from src.apps.auth.router import router as opt_router

router = APIRouter(prefix="/auth", tags=["Auth"])
router.include_router(opt_router)
