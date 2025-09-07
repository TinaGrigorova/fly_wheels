from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import os

SUPPORT_INBOX = os.environ.get("SUPPORT_INBOX", settings.DEFAULT_FROM_EMAIL)

def send_contact_email(name: str, email: str, message: str) -> int:
    subject = "New contact form submission"
    body = f"From: {name} <{email}>\n\n{message}"
    return send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [SUPPORT_INBOX])

def send_html_email(subject: str, html: str, to: list[str]) -> None:
    em = EmailMessage(subject, html, settings.DEFAULT_FROM_EMAIL, to)
    em.content_subtype = "html"
    em.send()
