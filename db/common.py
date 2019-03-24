# -*- coding: UTF-8 -*-
#!/usr/bin/python

import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="root",
  database="weibo"
)


