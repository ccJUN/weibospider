#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 入口文件 
import requests
import json
import re
import sys
from task import news 
import urllib
from flask import Flask
#from task import news

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return "hello world!"

if __name__=="__main__":
    app.run()
    word = urllib.quote('=60&q=啥是佩奇&t=4')
    originWord  = '啥是佩奇'
    number = 1
    for i in range(number):
        print(i)
        news.getNewsWeb('https://api.weibo.cn/2/cardlist?gsid=_2A25xibgPDeRxGeRK7VIZ8yvNzD6IHXVQH0zHrDV6PUJbkdAKLRPfkWpNU39zlV1ZOKI7rMvBWqnPw7jbN30b3vt4&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&lon=113.9288443990612&container_ext=show_topic%3A1&count=10&luicode=10000327&containerid=100103type'+word+'&featurecode=10000085&uicode=10000003&fid=100103type'+word+'&need_head_cards=0&lat=22.54346997882879&offset=1&need_new_pop=1&page='+str(i)+'&lfid=231619_3&moduleID=pagecard',word,originWord)