#importovanje biblioteke request koja nam omogućava vrlo jednostavan način za kreiranje GET,POST... zahteva ka serveru:
import requests

#pozivamo metodu get kojoj saljemo 2 argumenta
# URL-a koji je ovde http://127.0.0.1:8080/
# upitne stringove. Upitni stringovi se u requests pozivu prosleđuju u vidu tipa rečnik koji se dodeljuju argumentu params.
r = requests.get("http://127.0.0.1:8080/", params={"malo_sovo":'a'})
#ispisujemo povratnu vrednost metode get, statusni kod i podatke koje server vrati
print("Request method: GET, \
    Response status_code: {}, Response data: {}".format(r.status_code, r.text))

#pozivamo metodu post kojoj saljemo 2 argumenta
# URL-a koji je ovde http://127.0.0.1:8080/
# upitne stringove. Upitni stringovi se u requests pozivu prosleđuju u vidu tipa rečnik koji se dodeljuju argumentu params.
r = requests.post("http://127.0.0.1:8080/", params = {'malo_sovo':'e', 'veliko_slovo':'E'})
#ispisujemo povratnu vrednost metode get, statusni kod i podatke koje server vrati
print("Request method: POST, \
   Response status_code: {}, Response data: {}".format(r.status_code, r.text))
