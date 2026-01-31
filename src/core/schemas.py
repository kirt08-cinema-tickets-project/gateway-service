from pydantic import BaseModel, Field


# Request


# Response


class HealthResponse(BaseModel):
    status: str = Field(examples=["pong"])
    timestamp: str = Field(examples=["19:30:00-25/01/2026"])
