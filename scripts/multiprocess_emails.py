from asyncio.base_events import _SSLContext
import smtplib, ssl
from typing import Iterable, List
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import concurrent.futures

PORT: int = 465  # For SSL
SMTP_SERVER: str = "smtp.gmail.com"
SENDER_EMAIL: str = "####" 
PASSWORD: str = '####'


def send_mail(reciver_email: str, subject: str, body: str) -> bool:
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = reciver_email
    message['Subject'] = subject
    message['Bcc'] = reciver_email

    message.attach(MIMEText(body, 'plain'))
    text: str = message.as_string()

    context: ssl.SSLContext = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
            server.login(SENDER_EMAIL, PASSWORD)
            server.sendmail(SENDER_EMAIL, reciver_email, text)
            return True
    except Exception as e:
        print(f'<<<<<< {e} >>>>>>>')
        return False

def send_multiple_emails(addressants: List[str], subjects: List[str], bodies: List[str]) -> None:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results: Iterable  = executor.map(send_mail, addressants, subjects, bodies)

    print(f'{sum(results)} Out Of {len(addressants)} Sent Succesfuly')
