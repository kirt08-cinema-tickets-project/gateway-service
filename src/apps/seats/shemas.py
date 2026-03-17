from pydantic import BaseModel, Field


class Seat(BaseModel):
    id: str = Field(..., examples=["747e5a0e-e4b8-4bd0-88c8-838bc288fdff"])
    row: int = Field(..., examples=[1])
    number: int = Field(..., examples=[1])
    price: float = Field(..., examples=[350])
    status: str = Field(..., examples=["available"])
    type: str = Field(..., examples=["chair"])
    hallId: str = Field(..., examples=["d49a85d2-3ca4-4391-a48f-e7ccbb54e09b"])


class GetSeatResponse(BaseModel):
    seat: Seat

class ListSeatsResponse(BaseModel):
    seats: list[Seat]

