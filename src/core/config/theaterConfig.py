from pydantic import BaseModel


class TheaterConfig(BaseModel):
    host: str = ""
    port: str = ""