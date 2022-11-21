from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'clubmixfun@gmail.com'
email_password = 'aiuxwuxkinobybdf'

email_receiver = 'rbyuxtq006@tormails.com'

subject = "Check this video out!!"
body = """
a large heavy-bodied non-venomous snake occurring 
throughout the Old World tropics, killing prey by constriction and asphyxiation.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

