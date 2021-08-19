import smtplib
import time
import json
from random import randrange

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def load_json(file_name):
    d = None
    with open(file_name, 'r', encoding='utf-8') as outfile:
        d = json.load(outfile)
    return d

def send_mail(content, receiver):
    #The mail addresses and password
    sender_address = 'songkk2025@gmail.com'
    sender_pass = ''
    receiver_address = receiver
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Daily English'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(content, 'html'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

def make_message(idx, d):
    en = d[idx]['en']
    zh = d[idx]['zh']
   
    return """
    <div style="border:1px solid">
      <div style="color:red;font-size:18px">%s</div>
      <div style="margin-top:300px;color:blue;font-size:18px">%s</div>
    </div>
    """ % (zh, en)

if __name__ == '__main__':
    d = load_json('./combined/batch1_2_3-out.txt')
    size = len(d)
    print("total:", size)
    while True:
        idx = randrange(size)
        msg = make_message(idx, d)
        send_mail(msg, "tonylsf14@gmail.com")
        time.sleep(1800)
