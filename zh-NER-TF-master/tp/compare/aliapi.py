import urllib.request
import urllib
import sys

host = 'http://wbfxfc.market.alicloudapi.com'
path = '/rest/160601/text_analysis/aliws.json'
method = 'POST'
appcode = 'e73fb45a33584cb09549239f28a54d47'
querys = ''
bodys = {}
url = host + path

# bodys[''] = "{\"inputs\":[{\"text\":{\"dataType\":50,\"dataValue\":\"PAI算法平台\"}}]}"
post_data = {"dataType": 50,"dataValue":"PAI算法平台"}
rqs = urllib.request.Request(url, post_data)
rqs.add_header('Authorization', 'APPCODE ' + appcode)
# //根据API的要求，定义相对应的Content-Type
rqs.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(rqs)
content = response.read()
if (content):
    print(content)
