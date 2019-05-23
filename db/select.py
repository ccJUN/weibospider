#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mysql.connector
class Datebase:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="zhouwenyi1992",
            database="seo",
            charset="utf8"
        )
        
    def selectListen(self,mysqldb):
        db = self.conn.cursor()
        sql = "select web,name from "+mysqldb+" order by time"
        print(sql)
        db.execute(sql)
        results =db.fetchall()
        self.conn.commit()
        return results


    def selectRecord(self,mysqldb):
        db = self.conn.cursor()
        sql = "select web,record,time from "+mysqldb+" order by time"
        print(sql)
        db.execute(sql)
        results =db.fetchall()
        self.conn.commit()
        return str(results)

    def selectIp(self,mysqldb):
        db = self.conn.cursor()
        sql = "select uv,web,origin,time from "+mysqldb+" order by time"
        db.execute(sql)
        results =db.fetchall()
        self.conn.commit()
        return results

    def selectWebsites(self,mysqldb):
        db = self.conn.cursor()
        sql = "select web,top10,top20,top50,top100 from "+mysqldb+""
        db.execute(sql)
        results = db.fetchall()
        self.conn.commit()
        return str(results)
    
    def selectWeb(self,mysqldb):
        db = self.conn.cursor()
        sql = "select web, weights from "+mysqldb+""
        db.execute(sql)
        results = db.fetchall()
        print(results)
        self.conn.commit()
        return str(results)
    
