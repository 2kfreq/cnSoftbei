import pymysql
def insertSQL(SQL):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='raojun123', db='zhanhui', charset='utf8')
    cur=conn.cursor()
    cur.execute(SQL)
    conn.commit
    cur.close();
    conn.close();
