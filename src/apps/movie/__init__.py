from fastapi import APIRouter

from src.apps.movie.router import router as movie_router

router = APIRouter(prefix = "/movie", tags=["Movie"])
router.include_router(movie_router)