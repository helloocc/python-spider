# -*--coding:utf-8*-
import time
import os
from spider import Spider
from sender import Sender
from __builtin__ import str
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def check(new_data):
    file_title = []
    add_items = []

    # 获取当前文件夹的绝对路径
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, 'file')

    with open(file_path, 'r') as f:
        lines = (line.strip() for line in f)
        for line in lines:
            if len(line) > 0:
                title = line.split('#')[0]
                file_title.append(title)

    for house in new_data:
        if house['title'] not in file_title:
            add_items.append(house)

    if len(add_items) > 0:
        with open(file_path, 'w') as f:
            for house in new_data:
                print house['title'], house['price'], house['house_info']
                f.write(house['title'] + '#' + house['price'] + '#' + house['house_info'])
                f.write('\n')
    return add_items


if __name__ == "__main__":
    obj_spider = Spider()
    obj_sender = Sender()
    url = "https://hz.lianjia.com/ershoufang/rs%E5%8D%97%E5%B2%B8%E6%99%B6%E9%83%BD%E8%8A%B1%E5%9B%AD/"
    while True:
        try:
            hour = int(time.strftime('%H'))
            print time.strftime('%Y%m%d %H:%M:%S')

            if 0 < hour < 24:
                new_data = obj_spider.craw(url)
                add_items = check(new_data)
                if len(add_items) > 0:
                    print "New items!!!"
                    title = time.strftime('%Y%m%d %H:%M:%S')
                    content = ''
                    for house in add_items:
                        content += house['title'] + house['price'] + house['house_info'] + '\n'
                    obj_sender.send_email(title, content)
                else:
                    print "No change."
                time.sleep(20)
            else:
                time.sleep(3600)
        except Exception, e:
            print str(e)
