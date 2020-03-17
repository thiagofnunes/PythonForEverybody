import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url='http://py4e-data.dr-chuck.net/comments_382718.json'
connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode()
info = json.loads(data)
comments = info['comments']
print('Total comments',len(comments))
countSum=0
for item in comments:
    countSum = item['count'] + countSum
print(countSum)
