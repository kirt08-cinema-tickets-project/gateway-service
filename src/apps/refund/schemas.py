from pydantic import BaseModel, Field


class CreateRefundRequest(BaseModel):
    booking_id: str = Field(...)