import eshow
#import dm


a=input('请选择爬取的网站：\n1、大麦网\n2、展会网')
if int(a)==1:
    #空
    pass
if int(a)==2:
    month=input('请输入所爬取的月份：')
    print('开始爬取')
    eshow.eshowsearch(month)
    print('爬取完成！')
