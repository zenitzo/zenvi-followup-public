import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send_email(to_email, subject, body, from_email=None, password=None):
    """
    Sends an HTML email using SMTP with basic error handling.
    
    Raises:
        ValueError: if any input is invalid
        smtplib.SMTPException: for SMTP-level failures
    """
    if not to_email:
        raise ValueError("Missing recipient email address.")
    if not subject:
        raise ValueError("Missing subject line.")
    if not body:
        raise ValueError("Email body is empty.")

    # Fallback to .env if credentials not passed explicitly
    from_email = from_email or os.getenv("EMAIL_ADDRESS")
    password = password or os.getenv("EMAIL_PASSWORD")
    from_name = os.getenv("FROM_NAME", "")

    if not from_email or not password:
        raise ValueError("Missing sender credentials.")

    try:
        msg = MIMEMultipart("alternative")
        msg['From'] = f"{from_name} <{from_email}>" if from_name else from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        html_part = MIMEText(body, 'html')
        msg.attach(html_part)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())

    except smtplib.SMTPAuthenticationError:
        raise Exception("Failed to authenticate with SMTP server. Check email or password.")
    except smtplib.SMTPRecipientsRefused:
        raise Exception(f"SMTP server rejected recipient: {to_email}")
    except smtplib.SMTPException as e:
        raise Exception(f"SMTP error: {str(e)}")