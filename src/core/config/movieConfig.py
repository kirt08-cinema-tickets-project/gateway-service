from pydantic import BaseModel


class MovieConfig(BaseModel):
    host: str = ""
    port: str = ""