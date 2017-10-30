import time
import os
import glob

print(" ")
print("Doorbell.py started")

currentTime = time.strftime("Date:%m-%d-%y_Time:%H-%M-%S")

command = "bash PhotoTaker.sh" + " " + str(currentTime)
    
os.system(command)

print("Filename:", currentTime)

print("Starting Email.py")

emailCommand = 'python Email.py "Someone is at the door"' + ' "Photos/' + currentTime + '.jpg"'

os.system(emailCommand)

print("Process finished")

print("")
print("")
