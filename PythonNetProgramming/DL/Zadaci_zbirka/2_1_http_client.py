
import requests
r = requests.get("http://127.0.0.1:8080/", params={"name":'Pera'})
print("Request method: GET, Response status_code: {}, Response data: {}".format(r.status_code, r.text))


r = requests.post("http://127.0.0.1:8080/", params = {'name':'Nikola', 'last_name':'Nikolic'})
print("Request method: POST, Response status_code: {}, Response data: {}".format(r.status_code, r.text))
