'''Zadatak 1.6. Napraviti torku koja sadrži imena povrća. 
 Serijalizovati podatke(spakovati ih) pomoću json modula.  Ispisati taj objekat.
  Deserijalizovati objekat I ispisati torku.'''

#import modula
import json

#pravljenje torke
povrce_pre=('krompit','zelena salata','kupus','paradajz','paprika')

#ispis torke
print(povrce_pre)

#serijalizacija torke
o=json.dumps(povrce_pre)

#ispis objekta
print(o)

#deserijalizacija podatka
povrce_posle=json.loads(o)

#ispis torke
print(povrce_posle)