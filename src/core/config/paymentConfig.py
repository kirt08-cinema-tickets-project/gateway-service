from pydantic import BaseModel


class PaymentConfig(BaseModel):
    host: str = ""
    port: str = ""