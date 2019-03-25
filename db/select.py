import mysql.connector


def selectMysql(mysqldb):
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="zhouwenyi1992",
        database="weibo",
        charset="utf8"
    )
    cursor = db.cursor()
    sql = "SELECT anchor FROM "+mysqldb+" order by report"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.commit()
    db.close()
    return results

def selectHotweibo(mysqldb):
    cursor = db.cursor()
    sql = "SELECT * FROM "+mysqldb
    sql = cursor.execute(sql)
    print(sql)
    db.commit()
    db.close()
    return True
