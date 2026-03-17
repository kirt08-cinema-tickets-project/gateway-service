from pydantic import BaseModel


class ScreeningConfig(BaseModel):
    host: str = ""
    port: str = ""