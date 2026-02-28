from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.core.config.authConfig import AuthConfig
from src.core.config.usersConfig import UsersConfig
from src.core.config.loggerConfig import LoggerConfig
from src.core.config.cookiesCongig import CookiesConfig
from src.core.config.passportConfig import PassportConfig

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

class ModeConfig(BaseModel):
    mode : str = ""

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file = BASE_DIR / ".env",
        env_prefix = "GATEWAY_SERVICE__",
        env_nested_delimiter="__",
    )
    mode : ModeConfig = ModeConfig()
    logger : LoggerConfig = LoggerConfig() 
    auth : AuthConfig = AuthConfig()
    users : UsersConfig = UsersConfig()
    cookies : CookiesConfig = CookiesConfig()
    passport : PassportConfig = PassportConfig()
    
settings = Settings()