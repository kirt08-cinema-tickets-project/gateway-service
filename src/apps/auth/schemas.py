from typing_extensions import Self

from pydantic import BaseModel, model_validator, Field

from src.apps.auth.utils import Type_Enum
from src.apps.shared.schemas import (
    Email_Validate_Schema,
    Phone_Validation_Schema,
)


# Request
class SendOtpRequest(BaseModel):
    
    identifier: str = Field(min_length=5, max_length=100, examples=["+375447279809", "test@gmail.com"])
    type_identifier: Type_Enum

    @model_validator(mode="after")
    def validate_identidier(self) -> Self:
        if self.type_identifier == Type_Enum.email:
            try:
                x = Email_Validate_Schema(email=self.identifier)
                x.model_dump()
                self.identifier = x.email
            except Exception:
                raise ValueError("Incorrect Email")
        elif self.type_identifier == Type_Enum.phone:
            try:
                x = Phone_Validation_Schema(phone=self.identifier)
                x.model_dump()
                self.identifier = x.phone
            except Exception:
                raise ValueError("Incorrect Phone Number")
        return self

class VerifyOtpRequest(SendOtpRequest):
    code: str = Field(min_length=6, max_length=6, pattern=r'^\d+$') # string contains only digits

class TelegramVarifyRequest(BaseModel):
    fragment: str = Field(examples=["eyJpZCI6MTA4NjkxMjAwNSwiZmlyc3RfbmFtZSI6I..."])
    
# Response
