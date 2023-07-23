from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: str
    redis_user: str
    redis_password: str
    redis_host: str
    redis_port: str
    jwt_secret: str
    github_client_id: str
    github_client_secret: str

    class Config:
        env_file = '../.././env'


settings = None


def get_settings():
    global settings
    if settings is None:
        settings = Settings()  # type: ignore
    return settings
