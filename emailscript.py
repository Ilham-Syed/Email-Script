import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, message, from_email, to_email, password):
    # Create a message container
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    # Create SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Login to account
    server.login(from_email, password)

    # Send email
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()


# Example usage
subject = "Hello World"
message = "This is a test email sent using Python!"
from_email = ""#senders email
to_email = ""#receivers email
password = ""#password
send_email(subject, message, from_email, to_email, password)
