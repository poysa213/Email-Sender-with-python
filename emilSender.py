from email.message import EmailMessage

import ssl
import smtplib

email_sender = 'put your email'
email_password = "put on this a password that you should pick app from this link 'https://myaccount.google.com/apppasswords?rapt=AEjHL4NsuAEjWty6n99hKjGtklvxrXsLClmqz8lOd9xiGwEitxGam19oT8jpbdVcfspuVqoBq7531d8vqG2VD4J4ThopnHJpLg' add a app and name it python"

email_receiver = "put the reciver's email"

subject = "The subject"

body = """
write the body of email
"""

em = EmailMessage()

em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 456, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
