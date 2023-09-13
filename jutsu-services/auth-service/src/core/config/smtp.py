from fastapi_mail import ConnectionConfig

from src.core.config.settings import get_settings

settings = get_settings()

smtp_connection = ConnectionConfig(
    MAIL_USERNAME=settings.smtp.smtp_username,
    MAIL_PASSWORD=settings.smtp.smtp_password,
    MAIL_PORT=settings.smtp.smtp_port,
    MAIL_SERVER=settings.smtp.smtp_server,
    MAIL_FROM="notifications@devjutsu.io",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
)
