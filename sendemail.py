import smtplib, ssl

smtp_server = "smtp.gmail.com"
smtp_port = 465
password = input("Type your password and press ENTER: ")
sender = "serve.to.thrive@gmail.com"
receivers = "tuyendq@gmail.com"
message = """\
Subject: Send from python 3.x

This message is sent from Python 3.x."""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender,receivers, message)

