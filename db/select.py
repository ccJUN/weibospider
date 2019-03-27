#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mysql.connector

class Datebase:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="zhouwenyi1992",
            database="weibo",
            charset="utf8"
        )

    def selectMysql(self,mysqldb):
        db = self.conn.cursor()
        sql = "select distinct currentnode, anchor,report from "+mysqldb+" order by report desc"
        print(sql)
        db.execute(sql)
        results =db.fetchall()
        self.conn.commit()
        return results

    def sumReport(self,mysqldb):
        db = self.conn.cursor()
        sql = "select sum(distinct report) from "+mysqldb+" order by report"
        db.execute(sql)
        results =db.fetchall()
        self.conn.commit()
        return str(results)

    def selectTime(self,mysqldb):
        db = self.conn.cursor()
        sql = "select distinct currentnode, anchor,report,time from "+mysqldb+" order by time"
        db.execute(sql)
        results = db.fetchall()
        self.conn.commit()
        return results
