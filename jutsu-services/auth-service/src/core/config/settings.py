from enum import Enum
import os
from typing import Optional
from pydantic_settings import BaseSettings
from threading import Lock
from dotenv import load_dotenv


class Environment(str, Enum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"


class Base(BaseSettings):
    environment: Environment = Environment.DEVELOPMENT


class PostgresSettings(BaseSettings):
    postgres_user: Optional[str] = None
    postgres_password: Optional[str] = None
    postgres_db: Optional[str] = None
    postgres_host: Optional[str] = None
    postgres_port: Optional[int] = None


class RedisSettings(BaseSettings):
    redis_user: Optional[str] = None
    redis_password: Optional[str] = None
    redis_host: Optional[str] = None
    redis_port: Optional[int] = None


class TokenSecretSettings(BaseSettings):
    oauth_jwt_secret: Optional[str] = None
    reset_password_token_secret: Optional[str] = None
    verification_token_secret: Optional[str] = None


class GithubSettings(BaseSettings):
    github_client_id: Optional[str] = None
    github_client_secret: Optional[str] = None


class SMTPSettings(BaseSettings):
    smtp_server: Optional[str] = None
    smtp_port: Optional[int] = None
    smtp_username: Optional[str] = None
    smtp_password: Optional[str] = None


class Settings(BaseSettings):
    base: Base = Base()
    postgres: PostgresSettings = PostgresSettings()
    redis: RedisSettings = RedisSettings()
    token: TokenSecretSettings = TokenSecretSettings()
    github: GithubSettings = GithubSettings()
    smtp: SMTPSettings = SMTPSettings()

    @staticmethod
    def fetch_secrets():
        settings = Settings()
        load_dotenv()

        # Assign values from environment variables to settings
        if settings.base.environment == Environment.DEVELOPMENT:
            settings.postgres.postgres_user = os.getenv('POSTGRES_USER')
            settings.postgres.postgres_password = os.getenv(
                'POSTGRES_PASSWORD')
            settings.postgres.postgres_db = os.getenv('POSTGRES_DB')
            settings.postgres.postgres_host = os.getenv('POSTGRES_HOST')
            settings.postgres.postgres_port = os.getenv(
                'POSTGRES_PORT')  # type: ignore

            settings.redis.redis_user = os.getenv('REDIS_USER')
            settings.redis.redis_password = os.getenv('REDIS_PASSWORD')
            settings.redis.redis_host = os.getenv('REDIS_HOST')
            settings.redis.redis_port = os.getenv('REDIS_PORT')  # type: ignore

            settings.token.oauth_jwt_secret = os.getenv('OAUTH_JWT_SECRET')
            settings.token.reset_password_token_secret = os.getenv(
                'RESET_TOKEN_PASSWORD_SECRET')
            settings.token.verification_token_secret = os.getenv(
                'VERIFICATION_TOKEN_SECRET')

            settings.github.github_client_id = os.getenv('GITHUB_CLIENT_ID')
            settings.github.github_client_secret = os.getenv(
                'GITHUB_CLIENT_SECRET')

            settings.smtp.smtp_server = os.getenv('SMTP_SERVER')
            settings.smtp.smtp_port = os.getenv('SMTP_PORT')
            settings.smtp.smtp_username = os.getenv('SMTP_USERNAME')
            settings.smtp.smtp_password = os.getenv('SMTP_PASSWORD')
        else:
            pass


_settings = None
_settings_lock = Lock()


def get_settings():
    """
    Singleton function to get a settings object.
    This function will only initialize _settings once,
    and return the existing object for all subsequent calls.

    This function is thread-safe. In a multi-threaded or concurrent
    environment, it's possible that multiple threads might call
    this function at the same time. If there's no mechanism to
    ensure only one thread is allowed to initialize `_settings`,
    we could end up with a race condition: more than one thread
    might check `if _settings is None`, find that it's true
    (since `_settings` hasn't been initialized yet), and proceed
    to initialize `_settings`.

    By using a lock, we ensure that only one thread can initialize
    `_settings` to avoid such a scenario.

    Returns:
        Settings: The settings object.
    """
    global _settings
    # Check for the existence of _settings outside the lock first to avoid
    # unnecessary locking after _settings has been initialized
    if _settings is None:
        with _settings_lock:
            # Double-checked locking pattern to avoid initializing _settings
            # multiple times in case of concurrent calls to get_settings
            if _settings is None:
                _settings = Settings()
                _settings.fetch_secrets()
    return _settings
