'''
Created on Jun 4, 2016

@author: helloc
'''

import time
from getcity import GetCity
from collections import OrderedDict
from __builtin__ import str
import urllib2
import cookielib

def storeToFile(city_list):
    with open('citylist.txt', 'w') as f:
        for city in city_list:
            f.write(city)
            f.write('\n')
    return None

if __name__ == "__main__":
    url = "http://www.dianping.com/citylist/citylist?citypage=1" 
    city_list= GetCity().craw(url)
    storeToFile(city_list)


