from pydantic import BaseModel


class MediaConfig(BaseModel):
    host: str = ""
    port: str = ""