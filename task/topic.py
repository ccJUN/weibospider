# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import requests
import re
import json
import sys
import urllib
import time
import os
sys.path.append("..")
from db import insert
global_headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','charset':'utf-8'}

def getProxies():
    proxiesUrl = 'http://s.zdaye.com/?api=201903252034497979&count=1&px=2'
    res = requests.get(proxiesUrl,headers =global_headers)
    proxiesText = res.text
    return  proxiesText

def timestamp_datetime(value):
    format = '%a %b %d %H:%M:%S +0800 %Y'
    timeArray =  time.strptime(value,format)
    dt = time.mktime(timeArray)
    return  dt

def getNewsWeb(url,word,originWord,proxies):
    #关系链字典
    weiboSum = {}
    weibodict = {}
    weibodict['children'] = []
    weiboSum['children'] = []
    weibodict['name']= originWord
    weiboSum['name']= originWord
    # 初始化数据
    agent = proxies
    word = word
    # print('proxies',agent)
    try:
        url_word = urllib.quote(':60|t:4|pos:1-0-0|q:'+originWord+'|ext:&')
        res = requests.get(url,headers =global_headers,proxies=agent,timeout=30)
        content  = res.json()
        content = content['cards']
        # print('res',res)
    except:
        return 0
    for i  in range(len(content)):
        text = ''
        reposts_count = ''
        comments_count =''
        author = ''
        attitudes_count =''
        followers_count = ''
        created_at = ''
        card_group = content[i]['card_group']
        for j in range(len(card_group)):
            hots = card_group[j]
            try:
                timestamp = int(time.time())
                hot = hots['mblog']
                reposts_count = hot['reposts_count'] #转发次数
                comments_count = hot['comments_count'] #评论次数
                attitudes_count = hot['attitudes_count'] #点赞次数
                author = hot['user']['name'] #作者
                print(author)
                followers_count = hot['user']['followers_count'] #作者粉丝
                created_at = hot['created_at'] #微博时间
                text = hot['text'] #微博内容
                mid = hot['mid']
                idstr = hot['idstr']
                urlendecode_mid2 = urllib.quote('='+mid+'&')
                #  写入dict
                nextnode = {}
                nextnode['name']  = author
                nextnode['children'] =[]
                sumNextnode = {}
                sumNextnode['anchor'] = author
                sumNextnode['report']  = reposts_count
                sumNextnode['comment'] = comments_count
                sumNextnode['zan'] = attitudes_count
                sumNextnode['fans'] = followers_count
                sumNextnode['content'] = text
                sumNextnode['time'] = timestamp_datetime(created_at)
                sumNextnode['currentnode'] = idstr
                sumNextnode['nextnode'] = '0'
                sumNextnode['topic'] = '"'+originWord+'"'
                sumNextnode['description'] = hot['user']['description']
                insert.mysqlInsert('hotweibo',sumNextnode)
                # 获取热门的转发
                report_url = 'https://api.weibo.cn/2/statuses/repost_timeline?gsid=_2A25xibgPDeRxGeRK7VIZ8yvNzD6IHXVQH0zHrDV6PUJbkdAKLRPfkWpNU39zlV1ZOKI7rMvBWqnPw7jbN30b3vt4&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&id='+mid+'&mid='+mid+'&lcardid=seqid%3A1395807676%7Ctype'+url_word+'mid'+urlendecode_mid2+'qtime%3D'+str(timestamp)+'%26&pagesize=20&_status_id='+idstr+'&luicode=10000003&featurecode=10000085&uicode=10000002&rid=0_0_0_3068159735332620357_0_0_0&has_member=1&page=1&lfid=100103type'+word+'&moduleID=feed&sourcetype=page'
                reportRes = requests.get(report_url,headers =global_headers,proxies=agent)
                reportContent  = reportRes.json()['hot_reposts']
                sumNextnode['children'] = []
                # print('reportRes',reportRes)
                if(len(reportContent)>0):
                    nextnode['children'] = []
                    for i in range(len(reportContent)):
                        reportnode = {}
                        reportnode['anchor'] = reportContent[i]['user']['name']
                        reportnode['report'] = reportContent[i]['reposts_count']
                        reportnode['time'] = timestamp_datetime(reportContent[i]['created_at'])
                        reportnode['fans'] = reportContent[i]['user']['followers_count']
                        reportnode['description'] = reportContent[i]['user']['description']
                        reportnode['topic'] = '"'+originWord+'"'
                        reportnode['currentnode'] = idstr
                        reportnode['zan'] =  reportContent[i]['attitudes_count']
                        insert.mysqlInsert('hotreport',reportnode)
                        nextnode['children'].append(reportnode)
                        sumNextnode['children'].append(reportnode)
                weibodict['children'].append(nextnode)
                weiboSum['children'].append(sumNextnode)
            except:
                hot = '0'
    return weibodict['children']
