'''Zadatak 1.3 Napraviti rečnik koji za ključeve ima karaktere azbuke a kao vrednosti ima redni broj tog karaktera u azbuci.
 Ispisati rečnik. Otvoriti fajl ”azbuka” I upisati podatke rečnika kao objekte(serijalizovati podatke) uz pomoć marshal modula. 
 Podatke iz fajla deserijalizovati I ispisati na ekran.'''


#import modula
import marshal

#pravljenje recnika
abeceda_pre={"a":1,"b":2,"c":3}
#ispis recnika
print(abeceda_pre)

#otvaranje fajla i serijalizacija podataka
f = open("abeceda.pyc","wb")
marshal.dump(abeceda_pre, f)
f.close()

#otvaranje fajla i deserijalizacija podataka
f = open("abeceda.pyc","rb")
azbuka_posle = marshal.load(f)

#ispis recnika posle
print(azbuka_posle)

#zatvaranje fajla
f.close()
