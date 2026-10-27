from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "API_TEMPLATE"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "BOILERPLATE_FASTAPI_BASED"

    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "api_usuarios"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "1234"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
