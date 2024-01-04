import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, message, smtp_server, smtp_port, sender_email, sender_password):
    # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the message to the MIME object
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Use TLS encryption
            server.login(sender_email, sender_password)  # Log in to your email account

            # Send the email
            server.sendmail(sender_email, to_email, msg.as_string())
            print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print(f"SMTP Exception: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
to_email = 'to_email'
subject = 'Automated Email'
message = 'Hello, This is an automated email sent using Python.'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'sender_email'
sender_password = 'sender_password'

# Send the email
send_email(to_email, subject, message, smtp_server, smtp_port, sender_email, sender_password)
