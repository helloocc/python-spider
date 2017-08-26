# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText

class Sender(object):
    def send_email(self, title, content):
        mail_recipient = r'x@139.com'
        mail_host = "smtp.139.com"
        mail_sender = r"x@139.com"
        mail_pwd = "x"
        
        # 传入'plain'，最终的MIME就是'text/plain'
        mail_msg = MIMEText(content, 'plain', 'utf-8')
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


