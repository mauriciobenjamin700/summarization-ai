from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Attributes:
        DB_URL: Database connection URL
    """

    DB_URL: str = Field(default="")
    AI_MODEL: str = Field(default="")

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )


settings = Settings()
