from pydantic import Field

from src.apps.shared.schemas import (
    Email_Validate_Schema,
    Phone_Validation_Schema,
)


class InitEmailChangeRequest(Email_Validate_Schema):
    ...

class ConfirmEmailChangeRequest(Email_Validate_Schema):
    code: str = Field(min_length=6, max_length=6, pattern=r'^\d+$') # string contains only digits
 
class InitPhoneChangeRequest(Phone_Validation_Schema):
    ...

class ConfirmPhoneChangeRequest(Phone_Validation_Schema):
    code: str = Field(min_length=6, max_length=6, pattern=r'^\d+$') # string contains only digits