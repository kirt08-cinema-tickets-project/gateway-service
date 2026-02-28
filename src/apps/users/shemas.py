from typing import Optional
from pydantic import BaseModel, Field, EmailStr

from src.apps.shared.schemas import RU_BY_Phones_Numbers_Schema


class GetMeResponse(BaseModel):
    id: int = Field(examples=["1"])
    name: Optional[str] = Field(default=None, examples=["kirt"])
    avatar: Optional[str] = Field(default=None, examples=["kirt08.com/avatar/bshfbshefb2143214njsd"])
    phone: Optional[RU_BY_Phones_Numbers_Schema] = Field(default=None, examples=["+375446768905"])
    email: Optional[EmailStr] = Field(default=None, examples=["test@gmail.com"])
