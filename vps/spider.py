# -*--coding:utf-8*-
import time
import smtplib
from email.mime.text import MIMEText

import urllib2, re
from bs4 import BeautifulSoup
from collections import OrderedDict

class Spider(object):

        
    def craw(self, url):
        cont = self.download(url)
        res_data = self.parse(url, cont)
        self.output(res_data)
        return res_data.keys()
        
    def download(self, url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
    
    def parse(self, url, cont):
        if url is None or cont is None:
            return
        soup = BeautifulSoup(cont, 'html.parser', from_encoding='utf-8')
        res_data = OrderedDict()

        # http://s.dianping.com/event/nanjing 
        city = url.split("/")[4]
        res_data[city] = url
        
        # 此处会返回同一个event两次
        links = soup.find_all('a', href=re.compile(r"^/event/\d+"))
        
        # 将event的number和title加入到OrderedDict中，并去除重复
        for link in links :
            num = re.compile("\d+").search(link['href']).group()
            res_data[str(num)] = link['title']
        
        return res_data
    
    def output(self, data):
        fout = open('file', 'w')
        for key in data.iterkeys():
            fout.write(key + '\n')
        fout.close()
        
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

def check(new_data):
    file_data = []
    add_items = [] 
    
    with open('file', 'r') as f:
        lines = (line.strip() for line in f)
        for line in lines:
            file_data.append(line)
    
    for data in new_data:
        if data  not in file_data:
            add_items.append(data)
            file_data.insert(1, data)
            
    return add_items
            
          
if __name__ == "__main__":
    obj_spider = Spider()
    url = "http://s.dianping.com/event/nanjing" 

    while True:
        hour = int(time.strftime('%H'))
        print time.strftime('%Y%m%d %H:%M:%S')
       
        if hour >= 9 and hour <= 20: 
            new_data = obj_spider.craw(url)
            add_items = check(new_data)
            if(len(add_items) > 0):
                title = time.strftime('%Y%m%d %H:%M:%S')
                content = add_items
                send_email(title, content)
           
            time.sleep(20)
            
        elif hour < 8 or hour > 21:
            time.sleep(3598)
        else:
            time.sleep(1000)