import time
import os
import glob

print(" ")
print("Doorbell.py started")

now = time.strftime("Date:%m-%d-%y-Time:%H-%M-%S")

command = "bash PhotoTaker.sh" + " " + str(now)
    
os.system(command)

print("Filename:", now)

print("Starting Email.py")

emailCommand = 'python Email.py "Someone is at the door"' + ' "Photos/' + now + '.jpg"'

os.system(emailCommand)

print("Process finished")

print("")
print("")

