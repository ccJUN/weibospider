#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="weibo"
)

# 使用cursor()方法获取操作游标
mycursor = mydb.cursor()

# 使用execute方法执行SQL语句
mycursor.execute("CREATE TABLE hotweibo (id INT(64) NOT NULL AUTO_INCREMENT PRIMARY KEY,content TEXT, anchor VARCHAR(255), comment INT(64),report INT(64),fans INT(64),topic TEXT,zan INT(64),time TIMESTAMP,nextnode INT(64),currentnode INT(64))")

# 使用 fetchone() 方法获取一条数据
data = mycursor.fetchone()

# 关闭数据库连接
mydb.close()