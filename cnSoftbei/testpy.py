import re
def findpagenum(url):
    url=(url[50:])
    pagestr=''
    for a in afterurl:
        if re.match('[0-9]',str(a))!=None:
            pagestr+=(re.match('[0-9]',str(a))).group()
        else:
            break
    return int(pagestr)