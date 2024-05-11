'''Napraviti rečnik države_gradovi koji za ključeve sadrži imena država a vrednosti predstavljaju imena gradova. 
Ispisati rečnik. Otvoriti fajl ”drzave” I  upisati podatke rečnika kao objekte(serijalizovati podatke) uz pomoć pickle modula. 
Ispisati podatke iz fajla.  Podatke iz fajla deserijalizovati I ispisati na ekran.'''

#import modula
import pickle

#recnik
drzave_gradovi={'Srbija':'Beograd','Crna Gora':'Podgorica','Hrvatska':'Zagreb'}

#ispis recnika
print(drzave_gradovi)

#serijalizacija podataka i upis u fajl
with open('drzave', 'wb') as f: 
    pickle.dump(drzave_gradovi, f)

#ispis serijalizovanih podataka 
print(pickle.dumps(drzave_gradovi))

#citanje iz fajla i deserijalizacija
with open('drzave', 'rb') as f:
    s=pickle.load(f)

#ispis recnika posle deserijalizacije
print(s)