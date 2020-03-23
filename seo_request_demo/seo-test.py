import urllib2
import re
def getlist(keyword,pn=0):
    req = urllib2.Request('https://www.baidu.com/s?wd=%s&pn=%s' %(keyword,pn))
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
    html = urllib2.urlopen(req).read()
    reg = r'href = "(http://www\.baidu\.com/link\?url=(.*?))"'
    urls = re.findall(reg,html)
    for i in urls:
        req = urllib2.Request(i)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36')
        print urllib2.urlopen(req).read()
        break
getlist('seo')