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
def getProxies():
    proxiesUrl = 'http://s.zdaye.com/?api=201903252034497979&count=1&px=2'
    res = requests.get(proxiesUrl,headers =global_headers)
    proxiesText = res.text
    return  proxiesText


def getCosplay():
    number = 100
    weibo = {}
    for i in range(number):
        proxiesText = getProxies()
        proxies = {
            "http": "http://"+proxiesText.encode('ascii') ,
            "https": "https://"+proxiesText.encode('ascii'),
        }
        print(i,proxies)
        url = 'https://api.weibo.cn/2/cardlist?gsid=_2A25xnp7xDeRxGeRK7VIZ8yvNzD6IHXVQDZU5rDV6PUJbkdAKLRPfkWpNU39zlRRCwU-X39VgkiwJVbCEs0956zVR&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&lon=113.9287887904271&count=20&luicode=10000327&containerid=1087030002_2976_2001_5_hot&featurecode=10000233&uicode=10000327&fid=1087030002_2976_2001_5_hot&need_head_cards=0&lat=22.54344558548199&feed_mypage_card_remould_enable=1&offset=1&need_new_pop=1&page='+str(i+1)+'&lfid=1087030002_2975_2001&moduleID=pagecard'
        res = requests.get(url,headers =global_headers,proxies=proxies,timeout=30)
        content  = res.json()
        content = content['cards']
        for i  in range(len(content)):
            card_group = content[i]['card_group']
            for j in range(len(card_group)):
                cosplay = {}
                user = card_group[j]['user']
                cosplay['username'] = user['name']
                cosplay['fans'] = user['followers_count']
                cosplay['persondesc'] = card_group[j]['desc1'] + card_group[j]['desc2']
                userid = user['id']
                personUrl = 'https://api.weibo.cn/2/profile?gsid=_2A25xnp7xDeRxGeRK7VIZ8yvNzD6IHXVQDZU5rDV6PUJbkdAKLRPfkWpNU39zlRRCwU-X39VgkiwJVbCEs0956zVR&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&moduleID=pagecard&uicode=10000198&featurecode=10000233&luicode=10000327&dynamic_follow_button_menu_enable=1&user_domain='+str(userid)+'&lfid=1087030002_2976_2001_5_hot&lcardid=1087030002_2976_2001_5_hot_300080&sourcetype=page'
                res = requests.get(personUrl,headers =global_headers,proxies=proxies,timeout=30)
                person = res.json()
                cosplay['description'] = person['userInfo']['description']
                personid =  person['userInfo']['id']
                cosplay['tags'] = 0
                if(person['userInfo'].has_key('ability_tags')):
                    cosplay['tags'] =  person['userInfo']['ability_tags']
                
                containerid = person['tabsInfo']['tabs'][0]['containerid'].encode('ascii')
                print(personid,containerid)
                groupUrl = 'https://api.weibo.cn/2/cardlist?gsid=_2A25xnp7xDeRxGeRK7VIZ8yvNzD6IHXVQDZU5rDV6PUJbkdAKLRPfkWpNU39zlRRCwU-X39VgkiwJVbCEs0956zVR&sensors_mark=0&wm=3333_2001&i=6ad58d4&sensors_is_first_day=false&from=1093193010&b=0&c=iphone&networktype=wifi&skin=default&v_p=71&s=faf66666&v_f=1&sensors_device_id=9B9C5EE4-5B76-4605-BDF4-FF99705D8A87&lang=zh_CN&sflag=1&ua=iPhone10,3__weibo__9.3.1__iphone__os11.3&ft=11&aid=01Amd-yldu89BHuS4TwhgANlLd3xEbwvWa2lEeRqA7vHD1LWQ.&lcardid='+containerid+'_-_WEIBO_INDEX_PROFILE_DATA_FIELDGROUPTL&count=20&luicode=10000198&containerid=231051_-_followers_-_'+str(personid)+'_-_1042015%3AtagCategory_039&featurecode=10000233&uicode=10000011&fid=231051_-_followers_-_'+str(personid)+'_-_1042015%3AtagCategory_039&need_head_cards=1&feed_mypage_card_remould_enable=1&need_new_pop=1&page=1&sourcetype=page&moduleID=pagecard&lfid='+containerid+''
                print(groupUrl)
                res = requests.get(groupUrl,headers =global_headers,proxies=proxies,timeout=30)
                group = res.json()
                group = group['cards']
                groupdesc = 0
                for k in range(len(group)):
                    try:
                        if(group[k]['card_group'][0].has_key('desc')):
                            groupdesc = groupdesc+group[k]['card_group'][0]['desc']+','
                    except:
                        groupdesc = 0  
                cosplay['weibogroups'] =groupdesc
                insert.mysqlInsert('cosplay',cosplay)
    return '123'

if __name__=="__main__":
    getCosplay()