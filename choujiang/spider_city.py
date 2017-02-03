#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import urllib2
from bs4 import BeautifulSoup

class SpiderCity(object):

    def craw(self, url):
        cont = self.download(url)
        res_data = self.parse(url, cont)
        return res_data
        
    def download(self, url):
        print 'begin download...'
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
    
    def parse(self, url, cont):
        print 'begin parse...'
        if url is None or cont is None:
            return
        soup = BeautifulSoup(cont, 'html.parser', from_encoding='utf-8')

        food_types = soup.find_all('div', class_= "shop-gift")
        
        for food_type in food_types:
            if food_type.get_text().strip() == u'天天抽奖':
                return True
        
        return False
        
    
