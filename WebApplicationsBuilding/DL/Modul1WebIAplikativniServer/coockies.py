import requests
r = requests.get('https://httpbin.org/cookies/set', cookies={'cookie':'is_working'}) #vraca porsljedeno;takva struktura sajta
print(r.text)

r2 = requests.get("https://httpbin.org/cookies") #bez setovanja dobijamo prazan rijecnik, posto nista nismo poslali
print(r2.text)