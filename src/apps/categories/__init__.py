from fastapi import APIRouter

from src.apps.categories.router import router as category_router


router = APIRouter(prefix="/categories", tags=["categories"])
router.include_router(category_router)