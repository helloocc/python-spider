#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup
from collections import OrderedDict


class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/event/\d+"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(r's.dianping.com/', new_url)
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_data(self, page_url, soup):
        res_data = OrderedDict()
        
        res_data['url'] = page_url
      
        links = soup.find_all('a', href=re.compile(r"^/event/\d+"))
        
        for link in links :
            res_data[link['href']] = link['title']
            
#         for key, value in res_data.iteritems():
#             print key, value    
      
        return res_data
