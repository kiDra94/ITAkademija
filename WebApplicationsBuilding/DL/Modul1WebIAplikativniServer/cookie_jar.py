import requests
jar = requests.cookies.RequestsCookieJar()
jar.set('cookie', 'one', domain='httpbin.org', path='/cookies')
jar.set('cookie', 'two', domain='httpbin.org', path='/unknown')

'''Na ovaj način olakšavamo praćenje kolačića i rukovanje kolačićima kada moramo slati više različitih zahteva za različite domene ili stranice.
U našem primeru smo u bazu kolačića postavili dva kolačića: jedan koji će se proslediti kada se naš klijent poveže na httpbin.org/cookies i 
drugi koji će se proslediti kada se naš klijent 
poveže na httpbin.org/unknown. Ova druga varijanta sa putanjom /unknown ne postoji na serveru i korišćena je kao primer.'''

r = requests.get('https://httpbin.org/cookies', cookies=jar)
print(r.text)