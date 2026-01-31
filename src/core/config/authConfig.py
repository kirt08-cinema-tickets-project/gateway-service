from pydantic import BaseModel


class AuthConfig(BaseModel):
    host : str = "localhost"
    port : str = "50050"