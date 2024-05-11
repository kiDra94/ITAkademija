
import requests

r = requests.get("http://127.0.0.1:8080/", params={"malo_slovo":'a'})
print("Request method: GET, \
    Response status_code: {}, Response data: {}".format(r.status_code, r.text))

r = requests.post("http://127.0.0.1:8080/", params = {'malo_slovo':'e', 'veliko_slovo':'E'})
print("Request method: POST, \
   Response status_code: {}, Response data: {}".format(r.status_code, r.text))

r = requests.delete("http://127.0.0.1:8080/", params = {'malo_slovo':'d'})
print("Request method: DELETE, \
   Response status_code: {}, Response data: {}".format(r.status_code, r.text))
