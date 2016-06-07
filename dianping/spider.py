#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

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
