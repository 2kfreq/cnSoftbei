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
        self.Driver = webdriver.Chrome('chromedriver.exe')
        return super().__init__(**kwargs)

    def GetVocalConcert(self,begin_time="0",end_time="0",place=0):
        driver = self.Driver
        driver.get('https://search.damai.cn/search.html')
        ele_BeginDate = driver.find_element_by_xpath('//input[@id="from"]')
        ele_EndDate = driver.find_element_by_xpath('//input[@id="to"]')
        ele_BeginDate.send_keys(begin_time)
        ele_EndDate.send_keys(end_time,Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_link_text('演唱会').click()
        data = driver.page_source()
        print(data)
        # jsdata =js.loads(driver.page_source())
       
        # datalist = jsdata.keys()
        # for i in datalist:
        #     print(i)

    def GetPageData():
        urlstr='https://search.damai.cn/search.html'
        Req = urllib.request.Request(urlstr,headers=self.header)
        pagedata = urllib.request.urlopen(Req,timeout=5000).read()
        page = bt(pagedata,'lxml')
        print(page.prettify())


d = catchData()
d.GetVocalConcert(begintime='2017-06-23',endtime='2017-06-30')
