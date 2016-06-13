# -*--coding:utf-8*-
import time
from spider import Spider
from sender import Sender
from collections import OrderedDict

def check(new_data):
    file_data = OrderedDict()
    add_items = OrderedDict()
    
    with open('file', 'r') as f:
        lines = (line.strip() for line in f)
        for line in lines:
            if len(line) > 0:
                key = line.split('#')[0]
                value = line.split('#')[1]
                file_data[key] = value
    
    for key, value in new_data.iteritems():
        if key  not in file_data.iterkeys():
            add_items[key] = value
            
    if len(add_items) > 0:
            with open('file', 'w') as f:
                for key, value in new_data.iteritems():
                    f.write(key + '#' + value.encode('utf-8'))
                    f.write('\n')
    return add_items
            
          
if __name__ == "__main__":
    obj_spider = Spider()
    obj_sender = Sender()
    url = "http://s.dianping.com/event/nanjing/c1" 

    while True:
        hour = int(time.strftime('%H'))
        print time.strftime('%Y%m%d %H:%M:%S')
        
        if hour >= 9 and hour <= 18: 
            new_data = obj_spider.craw(url)
            add_items = check(new_data)
            if(len(add_items) > 0):
                print "New items!!!"
                title = time.strftime('%Y%m%d %H:%M:%S')
                content = "\n".join(add_items.values())
                obj_sender.send_email(title, content)
            else:
                print "No change."
            time.sleep(20)
             
        elif hour < 8 or hour > 20:
            time.sleep(3598)
        else:
            time.sleep(1000)
