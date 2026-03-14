from pydantic import BaseModel, Field

from fastapi import Path
from typing import Annotated


class Seat(BaseModel):
    id: str = Field(..., example="747e5a0e-e4b8-4bd0-88c8-838bc288fdff")
    row: int = Field(..., example=1)
    number: int = Field(..., example=1)
    price: float = Field(..., example=350)
    status: str = Field(..., example="available")
    type: str = Field(..., example="chair")
    hallId: str = Field(..., example="d49a85d2-3ca4-4391-a48f-e7ccbb54e09b")


class GetSeatResponse(BaseModel):
    seat: Seat

class ListSeatsResponse(BaseModel):
    seats: list[Seat]

