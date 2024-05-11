
import requests

r = requests.get("http://127.0.0.1:8080/", params={"drzava":'Srbija'})
print("Request method: GET, \
    Response status_code: {}, Response data: {}".format(r.status_code, r.text))

r = requests.post("http://127.0.0.1:8080/", params = {'drzava':'Bosna i Hercegovina', 'grad':'Sarajevo','povrsina':51209,'broj_stanovnika':3531159})
print("Request method: POST, \
   Response status_code: {}, Response data: {}".format(r.status_code, r.text))

r = requests.delete("http://127.0.0.1:8080/", params = {'drzava':'Srbija'})
print("Request method: DELETE, \
   Response status_code: {}, Response data: {}".format(r.status_code, r.text))
