from fastapi_mail import FastMail, MessageSchema

from src.core.config.smtp import smtp_connection


async def send_mail(subject, recipient, html_content):
    message = MessageSchema(
        subject=subject,
        recipients=[recipient],
        body=html_content,
        subtype="html"  # type: ignore
    )

    fm = FastMail(smtp_connection)
    await fm.send_message(message)
