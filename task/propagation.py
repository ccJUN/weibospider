#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 入口文件
import requests
import json
import time
import re
import sys
import urllib
sys.path.append("..")
from db import insert

global_headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','charset':'utf-8'}
weiboID=0
hotnumber=0
proxies = {}

def getProxies():
    time.sleep(15)
    proxiesUrl = 'http://api.xdaili.cn/xdaili-api//newExclusive/getIp?spiderId=2ebb6678b0934817aab5a6c3e9ac47c2&orderno=DX20194105958mPD2S&returnType=1&count=1&machineArea='
    res = requests.get(proxiesUrl,headers =global_headers,timeout=30)
    proxiesText = res.text
    return  proxiesText

def timestamp_datetime(value):
    format = '%a %b %d %H:%M:%S +0800 %Y'
    timeArray =  time.strptime(value,format)
    dt = time.mktime(timeArray)
    return  dt

def getWeibo():
    weibo = {}
    weiboid = 0
    try:
        proxiesText = getProxies()
        proxies = {
            "http": "http://"+proxiesText.strip('\n').encode('ascii'),
            "https": "https://"+proxiesText.strip('\n').encode('ascii'),
        }
        print(proxies)
        weiboUrl='https://api.weibo.cn/2/statuses/show?gsid=_2A25xpaycDeRxGeRK7VIZ8yvNzD6IHXVQ8qdUrDV6PUJbkdANLU6gkWpNU39zlU7nlFZWy1gAeHc99AXs5NzZ-vSj&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&id=4329480791503518&mid=4329738560510774&_status_id=4329480791503518&luicode=10000003&featurecode=10000085&uicode=10000002&rid=3_0_0_1413504540635004995_0_0_0&isGetLongText=1&has_member=1&lfid=231522type%3D60%26q%3D%23%E5%95%A5%E6%98%AF%E4%BD%A9%E5%A5%87%23%26t%3D0&moduleID=feed&lcardid=seqid%3A1358001130%7Ctype%3A60%7Ct%3A0%7Cpos%3A5-0-3%7Cq%3A%23%E5%95%A5%E6%98%AF%E4%BD%A9%E5%A5%87%23%7Cext%3A%26mid%3D4329738560510774%26qtime%3D1553753725%26'
        weiboRes = requests.get(weiboUrl,headers=global_headers,proxies=proxies,timeout=30)
        weiboContent = weiboRes.json()
        weiboid = weiboContent['id']
        weibo = {}
        weibo['anchor'] =  weiboContent['user']['name']
        weibo['fans'] =  weiboContent['user']['followers_count']
        weibo['location'] = weiboContent['user']['location']
        weibo['zan'] = weiboContent['attitudes_count']
        weibo['report'] = weiboContent['reposts_count']
        weibo['comment'] = weiboContent['comments_count']
        weibo['created_time'] = weiboContent['created_at']
        weibo['time'] = timestamp_datetime(weiboContent['created_at'])
        weibo['currentnode'] = weiboid
        weibo['prevnode'] = '0'
        weibo['nextnode'] = '0'
        weibo['content'] = weiboContent['text']
        weibo['verified_reason'] = weiboContent['user']['verified_reason']
        insert.mysqlInsert('start',weibo)
    except:
        print('getWeibo:error')
    return weiboid

def getHotTotal(mid,page,reportnumber,proxies):
    mid = mid
    hotUrl = 'https://api.weibo.cn/2/statuses/hot_repost_timeline?gsid=_2A25xpaycDeRxGeRK7VIZ8yvNzD6IHXVQ8qdUrDV6PUJbkdANLU6gkWpNU39zlU7nlFZWy1gAeHc99AXs5NzZ-vSj&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&moduleID=feed&id='+str(mid)+'&featurecode=10000085&count=20&page='+str(page)+''
    try:
        hotReq = requests.get(hotUrl,headers =global_headers,proxies=proxies,timeout=30)
    except:
        proxiesText = getProxies()
        proxies = {
            "http": "http://"+proxiesText.strip('\n').encode('ascii'),
            "https": "https://"+proxiesText.strip('\n').encode('ascii'),
        }
        hotReq = requests.get(hotUrl,headers =global_headers,proxies=proxies,timeout=30)
    HotContent = hotReq.json()
    hotRepostsList = HotContent['reposts']
    reportnumber = reportnumber + len(hotRepostsList)
    totalNumber = HotContent['total_number']
    num = totalNumber/reportnumber
    return num

def getHotReports1(mid,page,reportnumber,proxies):
    mid = mid
    hotUrl = 'https://api.weibo.cn/2/statuses/hot_repost_timeline?gsid=_2A25xpaycDeRxGeRK7VIZ8yvNzD6IHXVQ8qdUrDV6PUJbkdANLU6gkWpNU39zlU7nlFZWy1gAeHc99AXs5NzZ-vSj&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&moduleID=feed&id='+str(mid)+'&featurecode=10000085&count=20&page='+str(page)+''
    print(hotUrl)
    try:
        hotReq = requests.get(hotUrl,headers =global_headers,proxies=proxies,timeout=30)
        HotContent = hotReq.json()
    except:
        proxiesText = getProxies()
        proxies = {
            "http": "http://"+proxiesText.strip('\n').encode('ascii'),
            "https": "https://"+proxiesText.strip('\n').encode('ascii'),
        }
        hotReq = requests.get(hotUrl,headers =global_headers,proxies=proxies,timeout=30)
        HotContent = hotReq.json()
    hotRepostsList = HotContent['reposts']
    reportnumber = reportnumber + len(hotRepostsList)
    totalNumber = HotContent['total_number']
    for i in range(len(hotRepostsList)):
        weibo = {}
        weibo['anchor'] =  hotRepostsList[i]['user']['name']
        weibo['fans'] =   hotRepostsList[i]['user']['followers_count']
        weibo['location'] =  hotRepostsList[i]['user']['location']
        weibo['zan'] =  hotRepostsList[i]['attitudes_count']
        weibo['report'] =  hotRepostsList[i]['reposts_count']
        weibo['comment'] =  hotRepostsList[i]['comments_count']
        weibo['created_time'] =  hotRepostsList[i]['created_at']
        weibo['time'] = timestamp_datetime( hotRepostsList[i]['created_at'])
        weibo['currentnode'] = hotRepostsList[i]['id']
        weibo['prevnode'] = mid
        weibo['nextnode'] = '0'
        weibo['content'] =  hotRepostsList[i]['text']
        weibo['verified_reason'] =  hotRepostsList[i]['user']['verified_reason']
        print('1',weibo['anchor'])
        try:
            insert.mysqlInsert('start',weibo)
            getHotReports(hotRepostsList[i]['id'],1,0,proxies)
        except:
            print('error',reportnumber)

def getHotReports(mid,page,reportnumber,proxies):
    mid = mid
    hotUrl = 'https://api.weibo.cn/2/statuses/hot_repost_timeline?gsid=_2A25xpaycDeRxGeRK7VIZ8yvNzD6IHXVQ8qdUrDV6PUJbkdANLU6gkWpNU39zlU7nlFZWy1gAeHc99AXs5NzZ-vSj&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&moduleID=feed&id='+str(mid)+'&featurecode=10000085&count=20&page='+str(page)+''
    try:
        hotReq = requests.get(hotUrl,headers =global_headers,proxies=proxies,timeout=30)
        HotContent = hotReq.json()
    except:
        proxiesText = getProxies()
        proxies = {
            "http": "http://"+proxiesText.strip('\n').encode('ascii'),
            "https": "https://"+proxiesText.strip('\n').encode('ascii'),
        }
        hotReq = requests.get(hotUrl,headers =global_headers,proxies=proxies,timeout=30)
        HotContent = hotReq.json()
    hotRepostsList = HotContent['reposts']
    reportnumber = reportnumber + len(hotRepostsList)
    totalNumber = HotContent['total_number']
    try:
        for i in range(len(hotRepostsList)):
            weibo = {}
            weibo['anchor'] =  hotRepostsList[i]['user']['name']
            weibo['fans'] =   hotRepostsList[i]['user']['followers_count']
            weibo['location'] =  hotRepostsList[i]['user']['location']
            weibo['zan'] =  hotRepostsList[i]['attitudes_count']
            weibo['report'] =  hotRepostsList[i]['reposts_count']
            weibo['comment'] =  hotRepostsList[i]['comments_count']
            weibo['created_time'] =  hotRepostsList[i]['created_at']
            weibo['time'] = timestamp_datetime( hotRepostsList[i]['created_at'])
            weibo['currentnode'] = hotRepostsList[i]['id']
            weibo['prevnode'] = mid
            weibo['nextnode'] = '0'
            weibo['content'] =  hotRepostsList[i]['text']
            weibo['verified_reason'] =  hotRepostsList[i]['user']['verified_reason']
            print('2',weibo['anchor'])
            insert.mysqlInsert('start',weibo)
            getHotReports(hotRepostsList[i]['id'],1,0,proxies)
    except:
        print('error1',reportnumber)
    if(totalNumber > reportnumber):
        return getHotReports(mid,page+1,reportnumber,proxies)
    else:
        return '1'

if __name__=="__main__":
    weiboID = getWeibo()
    proxiesText = getProxies()
    proxies = {
        "http": "http://"+proxiesText.strip('\n').encode('ascii'),
        "https": "https://"+proxiesText.strip('\n').encode('ascii'),
    }
    num  = getHotTotal(weiboID,1,0,proxies)
    print('sum',num)
    for i in range(num):
        print('num:',i,weiboID,proxies)
        try:
            getHotReports1(weiboID,i+1,0,proxies)
        except:
            proxiesText = getProxies()
            proxies = {
                "http": "http://"+proxiesText.strip('\n').encode('ascii'),
                "https": "https://"+proxiesText.strip('\n').encode('ascii'),
            }
            getHotReports1(weiboID,i+1,0,proxies)
        time.sleep(300)