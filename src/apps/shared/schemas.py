from pydantic import BaseModel, EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumber


class Email_Validate_Schema(BaseModel):
    email: EmailStr


class RU_BY_Phones_Numbers_Schema(PhoneNumber):
    default_region_code = None
    supported_regions = ["RU", "BY"]
    phone_format = "E164"


class Phone_Validation_Schema(BaseModel):
    phone: RU_BY_Phones_Numbers_Schema = Field(examples=["+375447279809"])