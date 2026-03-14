from enum import Enum
from pydantic import BaseModel, Field


class SeatType(str, Enum):
    CHAIR = "chair"
    SOFA_2 = "sofa2"
    SOFA_3 = "sofa3"

class RowConfig(BaseModel):
    row: int = Field(...)
    columns: int = Field(...)
    type: SeatType = Field(...)
    price: int = Field(..., ge=0)

class CreateHallRequest(BaseModel):
    name: str = Field(..., examples=["hall1"])
    theater_id: str = Field(..., examples=["123456"])
    layouts: list[RowConfig]
