# -*- coding: UTF-8 -*-
import os
import re
import json
import sys
import time
import requests
import datetime
# import pytesseract
import sys
from bs4 import BeautifulSoup
from lxml import etree
sys.path.append("..")
from db import insert

headers={
    'Referer':'https://search.bilibili.com/all?keyword=%E5%92%8C%E5%B9%B3%E7%B2%BE%E8%8B%B1&from_source=banner_search&spm_id_from=333.334.b_62616e6e65725f6c696e6b.1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

videoUrl = []

class Bilibili(object):

    def getrank(self,url):
        print(url)
        res = requests.get(url,headers=headers)
        res.encode='utf-8'
        data = res.text
        rmdata = data.split('__jp0(')[1]
        rmdata = json.loads(rmdata[:-1])
        result = rmdata['data']['result']
        for i in range(len(result)):
            print(result[i]['author'])
            bilibilimysql = {}
            bilibilimysql['anchor'] = result[i]['author']
            bilibilimysql['description'] = result[i]['description']
            bilibilimysql['play'] = result[i]['play']
            r1 = '<em class="keyword">'
            r2 = '</em>'
            title = result[i]['title']
            title = re.sub(r1, '', title)
            title = re.sub(r2, '', title)
            print(title)
            bilibilimysql['title'] = title
            bilibilimysql['videourl'] = result[i]['arcurl']
            bilibilimysql['favorites'] = result[i]['favorites']
            bilibilimysql['duration'] = result[i]['duration']
            bilibilimysql['createtime'] = result[i]['pubdate']
            try:
                insert.mysqlInsert('bilibili',bilibilimysql)
            except:
                print('mysqlerror')
        return True

if __name__=='__main__':
    b = Bilibili()
    i = 0
    for i in range(50):
        b.getrank('https://api.bilibili.com/x/web-interface/search/type?search_type=video&highlight=1&keyword=%E5%92%8C%E5%B9%B3%E7%B2%BE%E8%8B%B1&from_source=banner_search&spm_id_from=333.334.b_62616e6e65725f6c696e6b.1&page='+str(i+1)+'&jsonp=jsonp&callback=__jp0')
