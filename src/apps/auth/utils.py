from enum import Enum

class Type_Enum(str, Enum):
    phone = 'phone'
    email = 'email'

class Roles(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"