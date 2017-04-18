import os
import json
from time import sleep
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


list_file = "lista.json"
trap_dir = "trapped"

if not os.path.exists(list_file):
    f = open(list_file, "w")
    json.dump({"files": []}, f)
    f.close()

def lister():
    files = set(os.listdir(trap_dir))
    f = open(list_file, "r")
    old = set(json.load(f)["files"])
    f.close()
    new = list(files.difference(old))
    f = open(list_file, "w")
    json.dump({"files": list(files)}, f)
    f.close()
    return new

def send_email(image):
    msg = MIMEMultipart()
    msg['Subject'] = "It's a trap!"
    msg['From'] = "nanook@nanook.com.br"
    msg['To'] = "nanook.labs@gmail.com"
    msg.preamble = "It's a trap!"

    with open(image, 'rb') as fp:
        img = MIMEImage(fp.read())
    msg.attach(img)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    s.login(user, pass)
    s.send_message(msg)
    s.quit()

while True:
    for i in lister():
        try:
            send_email(os.path.join(trap_dir, i))
        except Exception as e:
            print(e)
    sleep(5)

