from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PORT: str
    DB_NAME: str
    DB_PASS: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache
def settings() -> Settings:
    return Settings()
