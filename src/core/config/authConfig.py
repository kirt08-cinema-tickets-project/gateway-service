from pydantic import BaseModel


class AuthConfig(BaseModel):
    host : str = ""
    port : str = ""