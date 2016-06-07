#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import urllib2
from bs4 import BeautifulSoup
from collections import OrderedDict
import re

class Spider(object):
    def main(self):
        url = "http://s.dianping.com/event/nanjing"    
        obj_spider.craw(url)
        
    def craw(self, url):
        cont = self.download(url)
        data = self.parse(url, cont)
        self.output(data)
        
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
        data = OrderedDict()
        data['url'] = url
        links = soup.find_all('a', href=re.compile(r"^/event/\d+"))
        for link in links :
            data[link['href']] = link['title']
        return data
    
    def output(self, data):
        fout = open('output', 'w')
        for key, value in data.iteritems():
            print key, value
            fout.write(key + '\n')
        fout.close()
    
if __name__ == "__main__":
    obj_spider = Spider()
    obj_spider.main()
