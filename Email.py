from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys

print(" ")
print("Email.py started")

recipients = ["sam.park@live.com"]

emaillist = [elem.strip().split(',') for elem in recipients]

msg = MIMEMultipart()

msg['Subject'] = str(sys.argv[1])
msg['From'] = "<SprerryPi@gmail.com>"
msg['Reply-to'] = "SprerryPi@gmail.com"
 
msg.preamble = "Multipart massage.\n"
 
part = MIMEText("To whom ever it may concern, \n\nThere is some one at your door. \nA picture of this person has been attached.")

msg.attach(part)
 
part = MIMEApplication(open(str(sys.argv[2]),"rb").read())
part.add_header("Content-Disposition", "attachment", filename = str(sys.argv[2]))

msg.attach(part)
 

server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login("SprerryPi@gmail.com", "74108520")
 
server.sendmail(msg["From"], emaillist , msg.as_string())
