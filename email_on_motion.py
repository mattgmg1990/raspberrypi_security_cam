#! /usr/bin/python

import smtplib
import os
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

MOTION_OUTPUT_DIRECTORY = '/home/pi/motion'

SMTP_SERVER = 'smtp.gmail.com:587'

FROM_ADDRESS = "yourpi@pi.com"
TO_ADDRESSES = ["you@youremail.com", "person2@person2.com"]

COMMASPACE = ", "

# Credentials (might be better stored as an environment variable)
USERNAME = "yourpi@pi.com"
PASSWORD = "password"

def create_message():
    msg = MIMEMultipart()
    msg['Subject'] = 'Motion was detected at the front door!'
    msg['From'] = 'The Pi'
    msg['To'] = COMMASPACE.join(TO_ADDRESSES)
    msg.preamble = "Motion was detected by the security camera."
    msg_text = MIMEText("Motion was detected by the security camera. Please see the attached pictures, or check the live feed at: http://pi.mattgarnes.com:8081.")
    msg.attach(msg_text)

    # Get the last image taken and attach it
    filename = find_most_recently_modified_jpg_files(MOTION_OUTPUT_DIRECTORY)
    if not filename == '':
        image_file = open(MOTION_OUTPUT_DIRECTORY + '/' + filename, 'rb')
        img = MIMEImage(image_file.read())
        image_file.close()
        msg.attach(img)

    return msg

def send_email(msg):
    # Send the email
    server = smtplib.SMTP(SMTP_SERVER)
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(FROM_ADDRESS, TO_ADDRESSES, msg.as_string())
    server.quit()

# Does not count or return paths to symlinks
def find_most_recently_modified_jpg_files(dir_path):
    max_mtime = 0
    max_file = ''
    for dirname,subdirs,files in os.walk(dir_path):
        for fname in files:
            full_path = os.path.join(dirname, fname)
            if os.path.islink(full_path) or not 'jpg' in full_path:
                continue
            mtime = os.stat(full_path).st_mtime
            if mtime > max_mtime:
                max_mtime = mtime
                max_dir = dirname
                max_file = fname
    return max_file

msg = create_message()
send_email(msg)
