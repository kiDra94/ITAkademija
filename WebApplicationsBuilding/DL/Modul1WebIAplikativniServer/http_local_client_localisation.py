import requests
headers = {'Accept-Language': 'es'}
r = requests.get("http://127.0.0.1:8000/", headers = headers)
print("Request method: GET, \
    Response status_code: {}, Response data: {}".format(r.status_code, r.text))