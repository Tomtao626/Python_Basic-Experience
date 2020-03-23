# -*- coding:utf-8 -*-
import urllib.request
import re
def getlist(keyword,pn=0):
    req = urllib.request.Request('https://www.baidu.com/s?wd=%s&pn=%s' %(keyword,pn))
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
    html = urllib.request.urlopen(req).read()  #打开网页，获取网页源代码
    reg = r'href = "(http://www\.baidu\.com/link\?url=(.*?))"'  #（）表示建立索引
    img = re.compile(reg)
    html = html.decode('utf-8')
    imglist = re.findall(img,html)#urls列表
    for i in imglist:
        req = urllib.request.Request(i)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
        print(urllib.request.urlopen(req).read())
        break
    #print(len(imglist),imglist)
getlist('seo')