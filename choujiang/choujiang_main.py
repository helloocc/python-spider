'''
Created on Jun 4, 2016

@author: helloc
'''

from choujiang.spider_city import SpiderCity

def storeToFile(listName,fileName):
    with open(fileName, 'w') as f:
        for city in listName:
            f.write(city)
            f.write('\n')

def readFromFile():
    city_list=list()
    with open('citylist_main.txt', 'r') as reader:
        for line in reader:
            city_list.append(line)
    return city_list

if __name__ == "__main__":
#      get city list from url
#     url = "http://www.dianping.com/citylist/citylist?citypage=1" 
#     city_list= GetCity().craw(url)
#     storeToFile(city_list,'citylist.txt')

    city_list=readFromFile() 
    result=list()
    num=0
    for city in city_list:
        num+=1
        print num,':this is '+ city.strip()
        
        city_url="http://s.dianping.com/event/"+city
        isWanted = SpiderCity().craw(city_url)
        if isWanted:
            print city
            result.append(city)
           
    storeToFile(result, 'result.txt')
