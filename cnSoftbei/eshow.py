import pymysql
import requests
from bs4 import BeautifulSoup
import re
def eshowsearch(date):
    e365url='http://www.eshow365.com'
    date=str(date)
    if len(date)==1 :
        searchurl="http://www.eshow365.com/guonei/date-20170"+date+".html"
    else:
        searchurl="http://www.eshow365.com/guonei/date-2017"+date+".html"
    a=requests.get(searchurl,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3084.400 QQBrowser/9.6.11346.400'})
    a=BeautifulSoup(a.text,'lxml')
    b=a.find_all('a',attrs={'target':'_blank','href':re.compile(r'^/zhanhui/html/')})
    finalurl=[]
    for url in b:
        finalurl.append( e365url+url.get('href'))
    for url in finalurl:

        zhanhui=requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0'})
        zhanhui.encoding = 'utf8'
        zhanhui=BeautifulSoup(zhanhui.text,'lxml')
        name=zhanhui.find_all('h1')
        showtime=zhanhui.find_all('p');
        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='raojun123', db='zhanhui', charset='utf8')
        cur = conn.cursor()
        finalname=""
        finalcity=""
        finaltime=""
    
        for test in name:
            finalname=test.get_text().strip()
        for time in showtime:
            time=time.get_text().strip()
            if re.compile('^展会城市*').findall(time) :
                finalcity=(time[5:])
            if re.compile('^举办时间*').findall(time) :
                finaltime=(time[5:])
        cur.execute("INSERT INTO zhanhuidetail VALUES ('%s','%s','%s')"%(str(finalname),str(finalcity),str(finaltime)))
        conn.commit()
        cur.close()
        conn.close()
eshowsearch(8)