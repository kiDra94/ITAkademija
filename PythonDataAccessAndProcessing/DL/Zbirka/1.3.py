'''Zadatak 1.3 Napraviti rečnik koji za ključeve ima karaktere azbuke a kao vrednosti ima redni broj tog karaktera u azbuci.
 Ispisati rečnik. Otvoriti fajl ”azbuka” I upisati podatke rečnika kao objekte(serijalizovati podatke) uz pomoć marshal modula. 
 Podatke iz fajla deserijalizovati I ispisati na ekran.'''


import marshal
azbuka_pre={"a":1,"b":2,"c":3}
print(azbuka_pre)

f = open("azbuka.pyc","wb")
marshal.dump(azbuka_pre, f)
f.close()

f = open("azbuka.pyc","rb")
azbuka_posle = marshal.load(f)
print(azbuka_posle)
f.close()
