from pydantic import BaseModel


class UsersConfig(BaseModel):
    host: str = ""
    port: str = ""