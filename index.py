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
global_headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','charset':'utf-8'}
cookie = {
"ASP.NET_SessionId":"tmgbylku3jmm2vzjqpehikis"," .AspNet.ApplicationCookie":"2UeXV4lyd0nv4TP1qSdDHcj7plD-gzPruxUNW0QZfci6SJihfaZWfBB2YA3wYepjliOYt-kbk-Hq4TFSUqbrdQj_UIGmkvn8-ti1lHvZKiJSXgMWIfIPAM9W8OjsdBEpYwPgJAFzTY4a29JtywxgilrjGBGvbdT69jUrY1jKe5JWcWHDJI7952RjeB5C2vcVqyXV15BUJDRQrOLkSseQ-uPhQf4XJ_SYASU98nfUhfRQNW4aFPPg3Mh16gwTq33-7P_HPrg3b_VvzbvYVrJxhpkstW5k04EL0WgRZ6slLLUR4_SbzWXPSRK36XnWNJ8wLiNn8ouUJ50avXX0VSjQ7x8h6Is7w7I1HAdkodUYesb4a-ayAiO2redk0uS3QWFmPZSkHBQ-aaWFUBpKlBkKz1jz5HCwIzoLCjTpO1w8tOU"," Hm_lvt_f3b3086e3d9a7a0a65c711de523251a6":"1555297472"," Hm_lpvt_f3b3086e3d9a7a0a65c711de523251a6":"1555937286"
}

@app.route("/index")
def index():
    data = request.data.get("words")
    print(data)
    return True


#获取关联
@app.route("/getRelation",methods=['GET', 'POST'])
def getRelation():
    word  = '和平精英'
    urlEncodeWord = urllib.quote('=60&q=和平精英&t=1')
    print(urlEncodeWord)
    number = 100
    page  = []
    weibo = {}
    weibo['name'] = '和平精英'
    weibo['children'] = []
    
    for i in range(number):
        proxiesText = news.getProxies()
        proxies = {
            "http": "http://"+proxiesText.strip('\n').encode('ascii') ,
            "https": "https://"+proxiesText.strip('\n').encode('ascii'),
        }
        print(i,proxies)
        nodelist = news.getNewsWeb("https://api.weibo.cn/2/cardlist?gsid=_2A25x3j4DDeRxGeRK7VIZ8yvNzD6IHXVQyjbLrDV6PUJbkdANLU6gkWpNU39zlSWdFjjqXyGmrp8pSFDv5QE1Gk3e&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os12.2&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&lon=113.928804&extparam=%28null%29&container_ext=show_topic%3A1&count=10&luicode=10000003&containerid=100103type"+urlEncodeWord+"&featurecode=10000085&uicode=10000003&fid=100103type"+urlEncodeWord+"&need_head_cards=0&oid=1022%3A231522cba5fb32ba20f4fa77feeb522f17e37f&lat=22.543495&offset=1&need_new_pop=1&page="+str(i+10)+"&lfid=0&moduleID=pagecard&cum=39FAD1F5",urlEncodeWord,word,proxies)
        # nodelist = news.getNewsWeb('https://api.weibo.cn/2/cardlist?gsid=_2A25xs4hUDeRxGeRK7VIZ8yvNzD6IHXVQ6JycrDV6PUJbkdANLU6gkWpNU39zlR-2G3-SdByoHT91cp-unBxrY7tT&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&lon=113.9288443990612&container_ext=show_topic%3A1&count=10&luicode=10000327&containerid=100103type'+urlEncodeWord+'&featurecode=10000085&uicode=10000003&fid=100103type'+urlEncodeWord+'&need_head_cards=0&lat=22.54346997882879&offset=1&need_new_pop=1&page='+str(i+1)+'&lfid=231619_3&moduleID=pagecard',urlEncodeWord,word,proxies)
        # nodelist = news.getNewsWeb('https://api.weibo.cn/2/cardlist?gsid=_2A25xs4hUDeRxGeRK7VIZ8yvNzD6IHXVQ6JycrDV6PUJbkdANLU6gkWpNU39zlR-2G3-SdByoHT91cp-unBxrY7tT&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&lon=113.9288443990612&container_ext=show_topic%3A1&count=10&luicode=10000327&containerid=100103type'+urlEncodeWord+'&featurecode=10000085&uicode=10000003&fid=100103type'+urlEncodeWord+'&need_head_cards=0&lat=22.54346997882879&offset=1&need_new_pop=1&page='+str(i+1)+'&lfid=231619_3&moduleID=pagecard',urlEncodeWord,word,proxies)
        weibo['children'].append(nodelist)
    return json.dumps(weibo)


#数据读取
@app.route("/getlisten")
def getlisten():
    database = Datebase()
    data = database.selectListen('listen')
    data = ','.join(map(str,data))
    print(data)
    return data

#数据读取
@app.route("/getip")
def getip():
    database = Datebase()
    data = database.selectIp('ip')
    data = ','.join(map(str,data))
    return data

#
@app.route("/getrecord")
def getrecord():
    database = Datebase()
    sumReport = database.selectRecord('record')
    # print(sumReport)
    return sumReport

@app.route("/getwebsites",methods=['GET', 'POST'])
def getWebsites():
    data = request.args.get("web")
    websitesUrl  = 'https://www.5118.com/seo/included/'+data
    res = requests.get(websitesUrl,headers =global_headers,timeout=30,cookies=cookie)
    content  = res.text
    print(content)
    record = content.split('Site_INFO.ChartData = ')[1].split(';')[0]
    return record

@app.route("/getweb")
def getweb():
    database = Datebase()
    reporttime = database.selectWeb('web')
    data = ','.join(map(str,reporttime))
    return data


@app.route("/gettop",methods=['GET', 'POST'])
def gettop():
    data = request.args.get("web")
    # proxiesText = getProxies()
    # proxies = {
    #     "http": "http://"+proxiesText.strip('\n').encode('ascii'),
    #     "https": "https://"+proxiesText.strip('\n').encode('ascii'),
    # }
    # print(proxies)
    websitesUrl  = 'https://www.5118.com/seo/baidupc/'+data
    res = requests.get(websitesUrl,headers =global_headers,timeout=30,cookies=cookie)
    content  = res.text
    record = content.split('Site_INFO.ChartData = ')[1].split(';')[0]
    print(record)
    return record





def getProxies():
    proxiesUrl = 'http://api.xdaili.cn/xdaili-api//newExclusive/getIp?spiderId=2ebb6678b0934817aab5a6c3e9ac47c2&orderno=DX20194105958mPD2S&returnType=1&count=1&machineArea='
    res = requests.get(proxiesUrl,headers =global_headers)
    proxiesText = res.text
    return  proxiesText

if __name__=="__main__":
    app.run()