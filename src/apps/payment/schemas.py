from pydantic import BaseModel, Field

from src.apps.shared.schemas import SeatType


class InitPaymentRequest(BaseModel):
    screening_id: str = Field(...)
    seats: list[SeatType]
    payment_method_id: str | None = Field(default=None)
    save_payment_method: bool
