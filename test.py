import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL")
EMAIL_PASSWORD = os.getenv("PASSWORD")
RECIEVER = os.getenv("RECIEVER")

# Create email
msg = EmailMessage()
msg["Subject"] = "Test Email from Python"
msg["From"] = EMAIL_ADDRESS
msg["To"] = RECIEVER
msg.set_content("Hello Idriss, this is a test email sent using SMTP in Python.")

# Send email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.send_message(msg)

print("Email sent successfully!")