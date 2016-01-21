import urllib
import urllib2
import time
import xml.etree.cElementTree as ET
import cookielib

#build opener to use cookies (urlopen is a basic version of opener)
#create a file to save cookie info
filename = "bbscookie.txt"
cookie = cookielib.MozillaCookieJar(filename)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

starturl = "http://bbs.fudan.edu.cn/bbs/login"
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
accept_lan = "zh-TW, zh;q=0.8, en-US;q=0.6, en;q=0.4"
values = {'id': "", "pw": ""}
headers = {'User-Agent': user_agent, 'Referer': 'http://bbs.fudan.edu.cn/', 'Accept-Language': accept_lan}
data = urllib.urlencode(values)
request = urllib2.Request(starturl, data, headers)
response = opener.open(request)

#save the cookie info
cookie.save(ignore_discard = True, ignore_expires = True)



#page = response.read()
#print page
#print the cookie
#for item in cookie:
#    print 'Name = '+ item.name
#    print 'Value = '+ item.value


time.sleep(1)

url2 = "http://bbs.fudan.edu.cn/bbs/sec"
#request2 = urllib2.Request(url2, data, headers)
response2 = opener.open(url2)
tree = ET.ElementTree(response2)
root = tree.getroot()
print root
#print('root.tag =', root.tag)
#print('root.attrib =', root.attrib)

page = response2.read()
print page
