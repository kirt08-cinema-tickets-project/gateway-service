from fastapi import APIRouter

from src.apps.auth import router as auth_router
from src.apps.account import router as account_router
from src.apps.users import router as users_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(account_router)
router.include_router(users_router)
