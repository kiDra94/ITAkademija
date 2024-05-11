'''Zadatak 1.2. Napraviti torku koja sadrži imena voća.  Serijalizovati podatke(spakovati ih) pomoću pickle modula.
 Ispisati taj objekat. Deserijalizovati objekat I ispisati torku.'''


#import modula
import pickle

#pravljenje torke
voce_pre=('jabuka','kruska','banana','jagoda','borovnica')
#ispis torke
print(voce_pre)

#serijalizacija torke
o=pickle.dumps(voce_pre)
#ispis objekta
print(o)

#deserijalizacija podatka
voce_posle=pickle.loads(o)
#ispis torke
print(voce_posle)