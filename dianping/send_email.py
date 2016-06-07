# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
import time

def send_email(title, content):
    mail_recipient = r'helloc@wo.cn'
    mail_host = "smtp.wo.cn"
    mail_sender = r"helloc@wo.cn"
    mail_pwd = "xixi728"
    
    mail_msg = MIMEText(content, format, 'utf-8')
    mail_msg["Accept-Language"] = "zh-CN"
    mail_msg["Accept-Charset"] = "ISO-8859-1,utf-8"
    mail_msg['Subject'] = title
    mail_msg['From'] = mail_sender
    mail_msg['To'] = mail_recipient
    try:
        send = smtplib.SMTP()
        send.connect(mail_host)
        send.login(mail_sender, mail_pwd)
        send.sendmail(mail_sender, mail_recipient, mail_msg.as_string())
        send.close()
        print 'send success!'
        return True
    except Exception, e:
        print 'send failed!'
        print str(e)
        return False

# test    
if __name__ == '__main__':
    while True:
        hour = int(time.strftime('%H'))
        print hour
        if hour > 9 and hour < 16:
            title = time.strftime('%Y%m%d %H:%M:%S')
            content = u'你好'
            send_email(title, content)
        time.sleep(15)


        
