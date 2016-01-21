import urllib
import urllib2
import time
import xml.etree.cElementTree as ET 

url = "http://bbs.fudan.edu.cn/bbs/login"
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
accept_lan = "zh-TW, zh;q=0.8, en-US;q=0.6, en;q=0.4"
values = {'id': "", "pw": ""}
headers = {'User-Agent': user_agent, 'Referer': 'http://bbs.fudan.edu.cn/', 'Accept-Language': accept_lan}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)

#page = response.read()
#print page
time.sleep(1)

url2 = "http://bbs.fudan.edu.cn/bbs/sec"
request2 = urllib2.Request(url2, data, headers)
response2 = urllib2.urlopen(request)
tree = ET.ElementTree(response2)

page = response2.read()
print page
