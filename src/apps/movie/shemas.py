from typing import Optional
from pydantic import BaseModel, Field


class ListMoviesRequest(BaseModel):
    category: Optional[str] = Field(default=None, min_length=2, max_length=100, examples=["racing"])
    random: Optional[bool] = Field(default=False)
    limit: Optional[int] = Field(default=None, ge=1, le=100)
