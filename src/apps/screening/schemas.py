from pydantic import BaseModel, Field


class CreateScreeningRequest(BaseModel):
    movie_id: str = Field(...)
    hall_id: str = Field(...)
    start_at: str = Field(..., examples=["2026-03-17 13:00:00"])
    end_at: str = Field(..., examples=["2026-03-17 15:00:00"])

   

class GetScreeningsRequest(BaseModel):
    theater_id: str | None = Field(default=None)
    date: str | None = Field(default=None)