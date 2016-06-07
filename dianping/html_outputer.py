#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []


    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output', 'w')
        for data in self.datas:
            for key, value in data.iteritems():
                print key, value
                fout.write(key + '\n')
                
        fout.close()
