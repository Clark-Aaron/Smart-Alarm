#/!usr/bin python3

import re
from urllib import request

URL = "http://time.tianqi.com"

headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
        }

pattern = re.compile('<p id="times">(.*?)</p>')

def getTime(url:str=URL,headers:dict=headers,pattern=pattern) -> str:

        url = request.Request(URL,headers=headers)
        res = request.urlopen(url)
        html = res.read().decode('utf-8')
        content = re.search(pattern,html)
        return content.group(1)

if __name__ == "__main__":
        print(getTime())










