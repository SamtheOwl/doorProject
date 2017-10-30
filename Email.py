from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys

print(" ")
print("Email.py started")

recipients = ["someEmail@Email.com"]

emailList = [elem.strip().split(',') for elem in recipients]

msg = MIMEMultipart()

msg['Subject'] = str(sys.argv[1])
msg['From'] = "<otherEmail@otherMail.com>"
msg['Reply-to'] = "otherEmail@otherMail.com"
 
msg.preamble = "Multipart massage.\n"
 
part = MIMEText("To whom ever it may concern, \n\nThere is some one at your door. \nA picture of this person has been attached.")

msg.attach(part)
 
part = MIMEApplication(open(str(sys.argv[2]),"rb").read())
part.add_header("Content-Disposition", "attachment", filename = str(sys.argv[2]))

msg.attach(part)
 

server = smtplib.SMTP("smtp.otherMail.com:000")
server.ehlo()
server.starttls()
server.login("otherEmail@otherMail.com", "Password")
 
server.sendmail(msg["From"], emailList , msg.as_string())
