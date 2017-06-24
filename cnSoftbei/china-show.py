import pymysql
import requests
from bs4 import BeautifulSoup
import re
import mysql
def findpagenum(url):
    url=(url[50:])
    pagestr=''
    for a in afterurl:
        if re.match('[0-9]',str(a))!=None:
            pagestr+=(re.match('[0-9]',str(a))).group()
        else:
            break
    return int(pagestr)
def search(sdate,edate):
    max=0
    mini=10000
    sdate=str(sdate)
    edate=str(edate)
    mainurl='http://www.china-show.net/exhibit/search.php?kw=%D6%D0%B9%FA&fields=0&fromdate='+sdate+'&todate='+edate+'&catid=0&process=0&order=0&x=56&y=21'
    print(mainurl)
    openmainurl=requests.get(mainurl,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3084.400 QQBrowser/9.6.11346.400'})
    openmainurl=BeautifulSoup(openmainurl.text,'lxml')
    a=openmainurl.find_all('a')
    for b in a:
        b=b.get_text().strip()
        if re.match('[0-9][0-9]',b)==None:
            pass
        else:
            temp=int(re.match('[0-9][0-9]',b).group())
            if temp>max :
                max=temp
            if temp<mini:
                mini=temp
    for pagenum in range(1,max):
        mainurl='http://www.china-show.net/exhibit/search-htm-page-'+str(pagenum)+'-kw-%D6%D0%B9%FA-fields-0-fromdate-'+sdate+'-todate-'+edate+'-catid-0-process-0-order-0-x-67-y-16.html'
        openmainurl=requests.get(mainurl,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3084.400 QQBrowser/9.6.11346.400'})
        openmainurl=BeautifulSoup(openmainurl.text,'lxml')
        a=openmainurl.find_all('strong',{'class':'px14'})
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='raojun123', db='zhanhui', charset='utf8')
        cur = conn.cursor()
        for b in a:
            temp=str(b.get_text().strip())
            if temp=='抱歉，没有找到与“中国” 相关的内容。':
                break
            mysql.insertSQL("INSERT IGNORE INTO chinashow VALUES ('%s')"%(temp))
        print(pagenum)
search('20170601','20170622')