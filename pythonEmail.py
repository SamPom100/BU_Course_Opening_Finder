import smtplib
from email.message import EmailMessage
import json


def sendMail(subject, body):
    with open('secrets.json') as f:
        data = json.load(f)

    gmail_user = data['gmail_username']
    gmail_password = data['gmail_secret']

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = ''

    server.send_message(msg)
    server.quit()