from pydantic import BaseModel, SecretStr


class PassportConfig(BaseModel):
    hmac_domain : str = "test"
    secret_key : SecretStr = "123456"