# -*--coding:utf-8*-
from dianping.spider import Spider
import time
from dianping import send_email

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
        
        if hour >= 9 and hour <= 19: 
            new_data = obj_spider.craw(url)
            add_items = check(new_data)
            if(len(add_items) > 0):
                title = time.strftime('%Y%m%d %H:%M:%S')
                content = add_items
                send_email(title, content)
            time.sleep(20)
            
        elif hour < 8 or hour > 20:
            time.sleep(3598)
        else:
            time.sleep(1000)
                    
        


         
