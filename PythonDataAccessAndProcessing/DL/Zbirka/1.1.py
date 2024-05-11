'''Napraviti rečnik države_gradovi koji za ključeve sadrži imena država a vrednosti predstavljaju imena gradova. 
Ispisati rečnik. Otvoriti fajl ”drzave” I  upisati podatke rečnika kao objekte(serijalizovati podatke) uz pomoć pickle modula. 
Ispisati podatke iz fajla.  Podatke iz fajla deserijalizovati I ispisati na ekran.'''

import pickle

drzave_gradovi={'Srbija':'Beograd','Crna Gora':'Podgorica','Hrvatska':'Zagreb'}
print(drzave_gradovi)
with open('drzave', 'wb') as f: 
    pickle.dump(drzave_gradovi, f)

print(pickle.dumps(drzave_gradovi))

with open('drzave', 'rb') as f:
    s=pickle.load(f)

print(s)