'''Zadatak 1.6. Napraviti torku koja sadrži imena povrća. 
 Serijalizovati podatke(spakovati ih) pomoću json modula.  Ispisati taj objekat.
  Deserijalizovati objekat I ispisati torku.'''

import json

povrce_pre=('krompit','zelena salata','kupus','paradajz','paprika')
print(povrce_pre)

o=json.dumps(povrce_pre)
print(o)

povrce_posle=json.loads(o)
print(povrce_posle)