import requests
first_session = requests.Session()
first_session.cookies.update({'default_cookie': 'is_default'})
req_one = first_session.get('https://httpbin.org/cookies/set/cookie/is_working')
req_two = first_session.get('http://httpbin.org/cookies')
print("Second request response: ", req_two.text)

'''
U prethodnom primeru smo jednim get() pozivom nad linkom https://httpbin.org/cookies/set poslali željene kolačiće, 
a drugim pozivom get() metode nad linkom https://httpbin.org/cookies pokušali da ih iščitamo. Kako nije bilo reči o sesijskoj konekciji, 
prilikom iščitavanja dobili smo prazan odgovor. Prethodni primer u slučaju korišćenja sesije izgleda ovako:
'''