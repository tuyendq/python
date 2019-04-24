import smtplib, ssl, getpass
from cryptography.fernet import Fernet

def plain_text(file_key, file_cipher_text):
    """Return plain_text with provided paths of key and cipher_text files"""
    with open(file_key, 'r') as f:
        key = f.readline()
    with open(file_cipher_text, 'r') as f:
        cipher_text = f.readline()
    
    cipher_suite = Fernet(key)
    return cipher_suite.decrypt(cipher_text)

smtp_server = "smtp.gmail.com"
smtp_port = 587 # Use 465 for SMTPS
sender = "serve.to.thrive@gmail.com"
receivers = "tuyendq@gmail.com"
# print password # To cross check
message = """\
Subject: Send from python 2.x

This message is sent from Python 2.x."""

file_key = '/home/user/.keys/key' # plain text file stored key
file_cipher_text = '/home/user/.keys/cipher_text' # plain text file stored encrypted text
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    # uncomment to debug
    # server.set_debuglevel(1)
    
    server.ehlo()
    server.starttls()
    #server.login(sender, password)
    server.login(sender, plain_text(file_key, file_cipher_text))
    server.sendmail(sender,receivers, message)
    server.quit()
except Exception as e:
  print 'failed to send email'
  print(e)
