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

reload(sys)
sys.setdefaultencoding('utf-8')

global_headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1','charset':'utf-8'}
def getProxies():
    proxiesUrl = 'http://api.xdaili.cn/xdaili-api//newExclusive/getIp?spiderId=2ebb6678b0934817aab5a6c3e9ac47c2&orderno=DX20194105958mPD2S&returnType=1&count=1&machineArea='
    res = requests.get(proxiesUrl,headers =global_headers)
    proxiesText = res.text
    return  proxiesText

def getCosplay():
    url = 'https://lf.snssdk.com/api/news/feed/v78/?fp=PrT_LMQZc2s_FlT_LrU1F2KePMG1&version_code=6.7.8&app_name=news_article_lite&vid=74714645-C4BA-406F-8768-AF9F6B0702BA&device_id=53619778908&channel=App%20Store&resolution=1125*2436&aid=35&ab_version=770574,668905,374097,758002,770506,904370,643997,792518,661928,785656,800193,668907,808414,821460,772539,844798,846821,861726,668904,668906,877353,812272,894763,894990,895499,901422,770317,668903,679106,775316,894724,900975&ab_feature=201615,z2&review_flag=0&ab_group=z2,201615&update_version_code=6784&openudid=785bdb5300eb3701510b30962239dc8e962fb582&pos=5pe9vb%252F%252B9Onkv72nvb97Kix4AS6%252FsZe9vb%252Fx8vP69Ono%252Bfi%252Fvae9rKyus6SvpaWsr6muq66qr6WpsZe9vb%252Fx%252FOn06ej5%252BL%252B9p72vr7Ooqa6ppamvqaivqqyqpayX4A%253D%253D&idfv=74714645-C4BA-406F-8768-AF9F6B0702BA&ac=WIFI&os_version=12.2&ssmix=a&device_platform=iphone&iid=72616929738&ab_client=a1,f2,f7,e1&device_type=iPhone%20X&idfa=C22E9D1B-8CF2-4C1F-A379-25E3CBE4E52B&language=zh-Hans-CN&image=1&list_count=22&count=20&tt_from=pull&latitude=22.54348424527178&city=%E6%B7%B1%E5%9C%B3&last_refresh_sub_entrance_interval=1558424684&loc_time=1558424664&refer=1&refresh_reason=1&concern_id=6286225228934679042&longitude=113.9288124363728&session_refresh_idx=3&strict=0&LBS_status=authroize&detail=1&min_behot_time=1558424676&loc_mode=1&cp=5fCaEc30AcC6Cq1'
    res = requests.get(url,headers =global_headers,timeout=30)
    content  = res.json()
    data = content['data']
    for i in range(len(data)):
        jinri = {}
        datacontent = data[i]['content']
        datacontent = json.loads(datacontent)
        try:
            print('==================')
            print(datacontent['label'])
            print('==================')
            if datacontent['label'] =='广告':
                videotype = datacontent['has_video']
                jinri['title'] = datacontent['source']
                jinri['advertisers'] = datacontent['title']
                jinri['time'] = time.time()
                try:
                    jinri['url'] = datacontent['middle_image']['url']
                    print(datacontent['middle_image']['url'])
                except:
                    jinri['url'] = datacontent['display_url']
                try:
                    jinri['industry'] = '"'+str(datacontent['filter_words'][2]['name']).split(':')[1]+'"'
                    print(datacontent['filter_words'][2])
                except:
                    pass
                if videotype:
                    jinri['maintype'] = '"pic"'
                else:
                    jinri['maintype'] ='"video"'
                print('==================')
                print(jinri['maintype'])
                print('==================')
                insert.mysqlInsert('jinri',jinri)
        except:
            pass
    time.sleep(15)
    getCosplay()  
    return '123'

if __name__=="__main__":
    getCosplay()