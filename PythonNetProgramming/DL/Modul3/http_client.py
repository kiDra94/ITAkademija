import urllib.request
import urllib.parse

import requests

parsed_data = urllib.parse.urlencode({'first_name':'John', 'last_name':'Johnson'})
response = urllib.request.urlopen('https://httpbin.org/get')
 
print("URL: ",response.url)
 
print("Code: ",response.code)
 
print("Info: ", response.info())
 
print("Read: ", response.read())
 
print("Readlines: ",response.readlines())

print("--------------")
 
req = urllib.request.Request('https://httpbin.org/post',bytes(parsed_data, encoding = 'utf8'))
 
resp = urllib.request.urlopen(req)
 
print(resp.read())
#skidanje fajlova
urllib.request.urlretrieve('https://www.python.org/static/img/python-logo@2x.png', 'python_logo.png')
#skidanje pomocu request biblioteke
r = requests.get('https://www.python.org/static/img/python-logo@2x.png')
 
with open('python_logo.png', 'wb') as f:
    f.write(r.content)