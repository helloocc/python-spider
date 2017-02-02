'''
Created on Jun 4, 2016

@author: helloc
'''
import urllib2
import cookielib

# url = "http://www.baidu.com"
url = "http://www.dianping.com/citylist/citylist?citypage=1"

# print 'First method:'
# response1 = urllib2.urlopen(url)
# print response1.getcode()
# print len(response1.read())
# 
# print ''

# print 'Second method:'
# request = urllib2.Request(url)
# request.add_header("user-agent", "Mozilla/5.0")
# response2 = urllib2.urlopen(url)
# print response2.getcode()
# print len(response2.read())
# 
# print''

# print 'Third method:'
# cj=cookielib.CookieJar()
# opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# urllib2.install_opener(opener)
# response3=urllib2.urlopen(url)
# print response3.getcode()
# print cj 
# print response3.read()

print 'fourth method:'
site= "http://www.dianping.com/citylist/citylist?citypage=1"
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(site, headers=hdr)

try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()

content = page.read()
print content

