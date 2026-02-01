from typing_extensions import Self

from pydantic import BaseModel, model_validator, EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumber

from src.apps.auth.utils import Type_Enum


#Utils
class Email_Validate_Schema(BaseModel):
    email: EmailStr


class RU_BY_Phones_Numbers_Schema(PhoneNumber):
    default_region_code = None
    supported_regions = ["RU", "BY"]
    phone_format = "E164"


class Phone_Validation_Schema(BaseModel):
    phone: RU_BY_Phones_Numbers_Schema


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

# Response
