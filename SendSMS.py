import requests
from urllib import request,parse
import urllib
import json
import time
import re

for i in range(1,6):
    #请求手机号
    phoneurl = 'http://47.75.184.28/api/imessage-server/imessage-restapi/imessage/getContent?limit=100'
    req = requests.get(phoneurl)
    result = req.json()
    print(len(result))
    phones = ','.join(result)
    phone = re.sub(r",18205955365,123418966@qq.com,639392886366,16014863743", "", phones)  #17321042571,18205955365,123418966@qq.com,639392886366,16014863743
    newphone = phone.replace("17321042571", "17321042571,13917834931,13761742837,15738863912,18701819901,13127643643")
    print(newphone)
    now = time.strftime('%Y%m%d%H%M%S ', time.localtime(time.time()))
    sendurl = 'http://47.101.58.161:18002/send.do'
    textmob = {
        "uid": 9625,
        "pw": 494685,
        "mb": newphone,#'18501759629,15021003746'
        "ms": '【人人盈柒簲】跑得快、炸琻花、牪，補魚百種遊戲紸測聯系客服送禮金88元可提現，下傤送萬元大獎,?倘赚APP下傤:335294.cn 回T退订',
        "tm": now,

    }
    # print(textmob)
    req = requests.post(url=sendurl, data=textmob)
    status = req.status_code
    print(status)
    if status == 200:
        phonenum = re.sub("123418966@qq.com,","",phone)
        phdata = {
            "phoneno": phonenum,
        }
        ul = "http://www.aabapi.top/api/imessage-server/imessage-restapi/phone/updateSuccessPhone"
        r = requests.post(url=ul, data=phdata)
        s = r.status_code
        print("This batch of delivery status is {} ".format(s))
    else:
        continue
    time.sleep(30)
    i +=1

#每天8点定时执行脚本
# crontab -e

# 0 8 * * * python /Users/iwtay/Downloads/demo/Python-demo/SendSMS.py
