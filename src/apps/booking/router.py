from typing import Annotated
from fastapi import APIRouter, Depends

from src.apps.shared.service import authorized


router = APIRouter()


@router.get("/")
async def get_bookings(payload: Annotated[dict[str, str], Depends(authorized)]):
    user_id = payload.get("payload")
    return {
        "ok": True
    }