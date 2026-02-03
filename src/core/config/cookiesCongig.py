from pydantic import BaseModel, SecretStr


class CookiesConfig(BaseModel):
    domain : str = "localhost"