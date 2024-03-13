import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendEmail(subject, message, sender_email, receiver_emails, password):
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
