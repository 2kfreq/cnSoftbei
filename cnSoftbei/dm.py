from bs4 import BeautifulSoup as bt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import json as js
import time

class catchData(object):
    def __init__(self, **kwargs):
        self.header ={
            r'User-Agent':r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
            }
        #self.Driver = webdriver.Chrome('chromedriver.exe')
        return super().__init__(**kwargs)

    def GetVocalConcert(self,begin_time="0",end_time="0"):
        self.GetJsonData(begin_time,end_time)

    def GetPageData(self,data_list):
        str='https://piao.damai.cn/'
        for i in data_list:
            Req = urllib.request.Request(str+i+".html",headers=self.header)
            pagedata = urllib.request.urlopen(Req,timeout=5000).read()
            page = bt(pagedata,'lxml')
            showtime = page.find('div',class_='m-sdbox m-showtime').span.string
            venue = page.find('div',class_='m-sdbox m-venue').div.a.string
            title = page.find('h2',class_='tt').span.string
            print(title,venue,showtime,sep='|*-*|')
            time.sleep(2)    


    def GetJsonData(self,begin_time='0',end_time='0'):
        req_data={'ctl':'演唱会','st':begin_time,'et':end_time,'tsg':5}
        urlstr='http://search.damai.cn/search.html'
        urlstr1 = 'http://search.damai.cn/searchajax.html'
        data = urllib.parse.urlencode(req_data).encode('ascii')
        Req = urllib.request.Request(urlstr1,data,headers =self.header)
        pagedata = urllib.request.urlopen(Req).read()
        pagedata = pagedata.decode('utf8')
        jsondata = js.loads(pagedata)
        js_data_list=jsondata["ids"].split(",")
        self.GetPageData(js_data_list)
        



d = catchData()
d.GetVocalConcert(begin_time='2017-06-23',end_time='2017-06-23')
