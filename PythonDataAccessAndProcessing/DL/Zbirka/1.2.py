'''Zadatak 1.2. Napraviti torku koja sadrži imena voća.  Serijalizovati podatke(spakovati ih) pomoću pickle modula.
 Ispisati taj objekat. Deserijalizovati objekat I ispisati torku.'''



import pickle

voce_pre=('jabuka','kruska','banana','jagoda','borovnica')
print(voce_pre)

o=pickle.dumps(voce_pre)
print(o)

voce_posle=pickle.loads(o)
print(voce_posle)