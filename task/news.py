#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# weibo news 

import requests
import re
import json
import sys
import urllib
import time

global_headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','charset':'utf-8'}

def getNewsWeb(url,word,originWord):
    print(url)
    word = word
    url_word = urllib.quote(':60|t:4|pos:1-0-0|q:'+originWord+'|ext:&')
    res = requests.get(url,headers =global_headers)
    content  = res.json()
    content = content['cards']
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
                hot = hots['mblog']
                reposts_count = hot['reposts_count']
                comments_count = hot['comments_count']
                attitudes_count = hot['attitudes_count']
                author = hot['user']['name']
                followers_count = hot['user']['followers_count']
                created_at = hot['created_at']
                text = hot['text']
                mid = hot['mid']
                idstr = hot['idstr']
                urlendecode_mid2 = urllib.quote('='+mid+'&')
                timestamp = int(time.time())
                # 获取热门的转发
                #report_url ='https://api.weibo.cn/2/statuses/repost_timeline?gsid=_2A25xibgPDeRxGeRK7VIZ8yvNzD6IHXVQH0zHrDV6PUJbkdAKLRPfkWpNU39zlV1ZOKI7rMvBWqnPw7jbN30b3vt4&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&id=4330099744579393&mid=4330099744579393&lcardid=seqid%3A1395807676%7Ctype%3A60%7Ct%3A4%7Cpos%3A1-0-1%7Cq%3A%E5%95%A5%E6%98%AF%E4%BD%A9%E5%A5%87%7Cext%3A%26mid%3D4330099744579393%26qtime%3D1552895391%26&pagesize=20&_status_id=4330099744579393&luicode=10000003&featurecode=10000085&uicode=10000002&rid=1_0_0_3068159735332620357_0_0_0&has_member=1&page=1&lfid=100103type%3D60%26q%3D%E5%95%A5%E6%98%AF%E4%BD%A9%E5%A5%87%26t%3D4&moduleID=feed&sourcetype=page'
                report_url = 'https://api.weibo.cn/2/statuses/repost_timeline?gsid=_2A25xibgPDeRxGeRK7VIZ8yvNzD6IHXVQH0zHrDV6PUJbkdAKLRPfkWpNU39zlV1ZOKI7rMvBWqnPw7jbN30b3vt4&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&id='+mid+'&mid='+mid+'&lcardid=seqid%3A1395807676%7Ctype'+url_word+'mid'+urlendecode_mid2+'qtime%3D'+str(timestamp)+'%26&pagesize=20&_status_id='+idstr+'&luicode=10000003&featurecode=10000085&uicode=10000002&rid=0_0_0_3068159735332620357_0_0_0&has_member=1&page=1&lfid=100103type'+word+'&moduleID=feed&sourcetype=page'
                reportRes = requests.get(report_url,headers =global_headers)
                print(report_url,reportRes)
                reportContent  = reportRes.json()['hot_reposts']
                for i in range(len(reportContent)):
                    print('**************************************')
                    reposts_name = reportContent[i]['user']['name']
                    reposts_count = reportContent[i]['reposts_count']
                    reposts_created_at= reportContent[i]['created_at']
                    print(reposts_name)
                    print(reposts_count,reposts_created_at)
                    print('**************************************')
            except:
                hot = '0'
            print('=========================')
            print(text)
            print(author)
            print('reposts_count:',reposts_count)
            print('attitudes_count:',attitudes_count)
            print('comments_count',comments_count)
            print('created_at',created_at)
            print('fans',followers_count)
            print(idstr,mid)
            print('=========================')
    return True

