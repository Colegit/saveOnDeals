import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, message, sender_email, receiver_emails, password):
    # Create a MIMEText object to represent the email body
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(receiver_emails)  # Concatenate multiple email addresses with a comma
    msg['Subject'] = subject

    # Attach the message to the MIMEText object
    msg.attach(MIMEText(message, 'plain'))

    # Connect to Gmail's SMTP server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    # Login to your Gmail account
    server.login(sender_email, password)

    # Send the email to each recipient
    for receiver_email in receiver_emails:
        server.sendmail(sender_email, receiver_email, msg.as_string())

    # Close the connection to the SMTP server
    server.quit()

# Set your Gmail account credentials
sender_email = 'your@gmail.com'  # Your Gmail address
receiver_emails = ['recipient1@gmail.com', 'recipient2@gmail.com']  # List of recipient email addresses
password = 'your_password'  # Your Gmail password

# Example usage
subject = 'Price Drop Alert'
message = 'The price dropped below the target.'

send_email(subject, message, sender_email, receiver_emails, password)