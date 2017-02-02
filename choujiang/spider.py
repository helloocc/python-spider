#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import urllib2, re
from bs4 import BeautifulSoup
from collections import OrderedDict

class Spider(object):

    def craw(self, url):
        cont = self.download(url)
        res_data = self.parse(url, cont)
        return res_data
        
    def download(self, url):
        print 'begin download...'
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
        req = urllib2.Request(url, headers=hdr)
        try:
            page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            return e.fp.read()
        content = page.read()
        return content
    
    def parse(self, url, cont):
        print 'begin parse...'
        if url is None or cont is None:
            return
        soup = BeautifulSoup(cont, 'html.parser', from_encoding='utf-8')
        city_list = list()
        print url
        
        links = soup.find_all('a', href=re.compile(r"^/[a-z]+$"))
      
        for link in links :
            city=re.compile("[a-z]+").search(link['href']).group()
            city_list.append(city)
        return city_list
    
