from pydantic_settings import BaseSettings
from pydantic import field_validator, model_validator


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DATABASE_URL: str = ""
    SECRET_KEY: str
    ALGORITHM:str

    @model_validator(mode='after')
    def assemble_db_url(self) -> 'Settings':
        self.DATABASE_URL = (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
        return self

    model_config = {
        "env_file": ".env"
    }


settings = Settings()