from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_HTTP_CLIENT_TIMEOUT: float = 5.0

    SENTRY_DSN: str = ''

    BSG_URL: str
    BSG_API_KEY: str
    BSG_SENDER_NAME: str


settings = Settings()
