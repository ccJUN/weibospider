#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mysql.connector

def mysqlInsert(mysqldb,mysqlstring):

    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="zhouwenyi1992",
        database="weibo",
    )
    cursor = db.cursor()
    InsertString = mysqlstring
    mysqlContent = '('
    mysqlKey = '('
    for (key,value) in InsertString.items():
        # print(type(value))
        if(key==InsertString.keys()[-1] ):
            mysqlKey=mysqlKey+str(key).encode('utf-8')
            if(type(value)== unicode):
                mysqlContent = mysqlContent+"'"+value.encode('utf-8')+"'"
            else:
                mysqlContent = mysqlContent+str(value)
        else:
            if(type(value)== unicode):
                mysqlContent = mysqlContent+"'"+value.encode('utf-8')+"',"
            else:
                mysqlContent = mysqlContent+str(value)+','
            mysqlKey=mysqlKey+str(key).encode('utf-8')+','
    mysqlContent=mysqlContent+')'
    mysqlKey=mysqlKey+')'
    sql = " INSERT INTO  " +mysqldb + mysqlKey + " VALUES  " +mysqlContent
    print(sql)
    cursor.execute(sql)
    db.commit()
    db.close()
    return True