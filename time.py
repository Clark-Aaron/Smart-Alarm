#/!usr/bin python3

import re
from urllib import request

URL = "http://time.tianqi.com"

headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
        }
url = request.Request(URL,headers=headers)

res = request.urlopen(url)

html = res.read().decode('utf-8')
#print(html)

pattern = re.compile('<p id="times">(.*?)</p>')

content = re.search(pattern,html)

print(content.group(1))








