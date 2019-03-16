#!/usr/bin/python

import smtplib

from email.mime.text import MIMEText

textfile = "/tm/textfile"

fp = open('/tmp/textfile', 'rb')

msg = MIMEText(fp.read())
fp.close()

smtp_server_host = "smtp.gmail.com"
smtp_server_port = 465
sender = "serve.to.thrive@gmail.com"
receivers = "[tuyendq@gmail.com]"

msg['Subject'] = 'The content of %s' % textfile
msg['From'] = sender
msg['To'] = receivers

try:
    print("Sending message: " + msg['Subject']
    smtplib.SMTP_SSL(smtp_server_host, smtp_server_port)
    s.login(sender,"yourpassword")
    s.sendmail(sender, receivers, msg.as_string())
    s.quit()
    print("message send")
except smtplib.SMTPException:
    print("Could not send email)
