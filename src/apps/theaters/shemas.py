from pydantic import BaseModel


class TheaterCreateRequest(BaseModel):
    name: str
    address: str