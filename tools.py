import smtplib

from datetime import datetime
from email.mime.text import MIMEText

def mail_send(mail_from, mail_to, mail_subject, mail_body):
   
    msg = MIMEText(mail_body.encode('UTF-8'),"html",'UTF-8')
    msg['Subject'] = mail_subject;
    msg['From'] = mail_from
    msg['To'] = ", ".join(mail_to)
   
    #fail silently
    try:
        s = smtplib.SMTP('localhost')
        s.sendmail(mail_from, mail_to, msg.as_string())
        s.quit()
    except:
        return -1

