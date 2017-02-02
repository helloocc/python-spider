'''
Created on Jun 4, 2016

@author: helloc
'''

import time
from spider import Spider
from collections import OrderedDict
from __builtin__ import str
import urllib2
import cookielib


if __name__ == "__main__":
    obj_spider = Spider()
    url = "http://www.dianping.com/citylist/citylist?citypage=1" 
    city_list=obj_spider.craw(url)
    for city in city_list:
        print city

