'''Zadatak 1.4. Napraviti string. Serijalizovati string(spakovati ga) pomoću marshal modula. Ispisati objektat.
 Deserijalizovati objekat I ispisati string.'''

#import modula
import marshal

#pravljenje stringa
string_pre="ITA"

#ispis stringa
print(string_pre)

#serijalizacija podatka
o=marshal.dumps(string_pre)

#ispis objekta
print(o)

#deserijalizacija podatka
string_posle=marshal.loads(o)

#ispis stringa
print(string_posle)