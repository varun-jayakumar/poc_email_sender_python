import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()  


# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')
recipient_email = 'varunbharathi.j@gmail.com'

# Create the email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = 'Test Email from Python Script'

# Email body
body = 'This is a test email sent from a Python script!'
message.attach(MIMEText(body, 'plain'))

try:
    # Set up the server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)
    
    # Send the email
    server.sendmail(sender_email, recipient_email, message.as_string())
    print('Email sent successfully!')
    
except Exception as e:
    print(f'Error: {e}')
    
finally:
    server.quit()
