from fastapi import APIRouter

from src.apps.account.router import router as account_router

router = APIRouter(prefix="/account", tags=["Account"])
router.include_router(account_router)
