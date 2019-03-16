import smtplib, ssl, getpass

smtp_server = "smtp.gmail.com"
smtp_port = 587 # Use 465 for SMTPS
sender = "serve.to.thrive@gmail.com"
receivers = "tuyendq@gmail.com"
# print password # To cross check
message = """\
Subject: Send from python 2.x

This message is sent from Python 2.x."""

try:
    password = getpass.getpass("Type password of '" + sender + "' and press ENTER: ")
    server = smtplib.SMTP(smtp_server, smtp_port)
    # uncomment to debug
    # server.set_debuglevel(1)
    
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender,receivers, message)
    server.quit()
except Exception as e:
  print 'failed to send email'
  print(e)
