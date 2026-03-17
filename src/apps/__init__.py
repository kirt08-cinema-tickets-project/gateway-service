from fastapi import APIRouter

from src.apps.auth import router as auth_router
from src.apps.account import router as account_router
from src.apps.users import router as users_router
from src.apps.movie import router as movie_router
from src.apps.categories import router as categories_router
from src.apps.theaters import router as theaters_router
from src.apps.halls import router as halls_router
from src.apps.seats import router as seats_router
from src.apps.screening import router as screening_router


router = APIRouter()

router.include_router(auth_router)
router.include_router(account_router)
router.include_router(users_router)
router.include_router(movie_router)
router.include_router(categories_router)
router.include_router(theaters_router)
router.include_router(halls_router)
router.include_router(seats_router)
router.include_router(screening_router)
