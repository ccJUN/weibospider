#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 入口文件
import requests
import json
import time
import re
import sys
from db.select import Datebase
from task import news
import urllib
from flask import Flask
from flask_cors import CORS
from flask import request

#from task import news

app = Flask(__name__)
CORS(app, resources=r'/*')
app.debug = True

@app.route("/")

@app.route("/scrapy",methods=['GET', 'POST'])
def scrapy():
    data = request.data.get("words")
    print(data)
    return True


#获取关联
@app.route("/getRelation",methods=['GET', 'POST'])
# 采集器
def getRelation():
    word  = '啥是佩奇'
    urlEncodeWord = urllib.quote('=60&q=#啥是佩奇#&t=1')
    number = 1
    page  = []
    weibo = {}
    weibo['name'] = '啥是佩奇'
    weibo['children'] = []
    for i in range(number):
        proxiesText = news.getProxies()
        proxies = {
            "http": "http://"+proxiesText.encode('ascii'),
            "https": "https://"+proxiesText.encode('ascii'),
        }
        print(i,proxies)
        # nodelist = news.getNewsWeb('https://api.weibo.cn/2/cardlist?gsid=_2A25xibgPDeRxGeRK7VIZ8yvNzD6IHXVQH0zHrDV6PUJbkdAKLRPfkWpNU39zlV1ZOKI7rMvBWqnPw7jbN30b3vt4&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&lon=113.9288045989115&container_ext=show_topic%3A1&count=10&luicode=10000327&containerid=100103type%3D1%26q%3D%E5%95%A5%E6%98%AF%E4%BD%A9%E5%A5%87%26t%3D2&featurecode=10000085&uicode=10000003&fid=100103type%3D1%26q%3D%E5%95%A5%E6%98%AF%E4%BD%A9%E5%A5%87%26t%3D2&need_head_cards=0&lat=22.54347427757234&offset=1&need_new_pop=1&page='+str(i)+'&lfid=231619_3&moduleID=pagecard',urlEncodeWord,word)
        nodelist = news.getNewsWeb('https://api.weibo.cn/2/cardlist?gsid=_2A25xmyB5DeRxGeRK7VIZ8yvNzD6IHXVQ8TSxrDV6PUJbkdAKLRPfkWpNU39zlUCZbdyUmmzc2X7mHKib4O59BmYv&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&lon=113.9288443990612&container_ext=show_topic%3A1&count=10&luicode=10000327&containerid=100103type'+urlEncodeWord+'&featurecode=10000085&uicode=10000003&fid=100103type'+urlEncodeWord+'&need_head_cards=0&lat=22.54346997882879&offset=1&need_new_pop=1&page='+str(i+1)+'&lfid=231619_3&moduleID=pagecard',urlEncodeWord,word,proxies)
        time.sleep(15)
        weibo['children'].append(nodelist)
    return json.dumps(weibo)
#数据读取
@app.route("/gethotrepeat")
def gethotrepeat():
    database = Datebase()
    data = database.selectMysql('hotweibo')
    data = ','.join(map(str,data))
    return data

#
@app.route("/getSum")
def getsum():
    database = Datebase()
    sumReport = database.sumReport('hotweibo')
    print(sumReport)
    return  sumReport

@app.route("/getNextHotRepeat")
def getNextHotRepeat():
    return True

@app.route("/getTime")
def getTime():
    database = Datebase()
    reporttime = database.selectTime('hotweibo')
    data = ','.join(map(str,reporttime))
    return data


if __name__=="__main__":
    app.run()