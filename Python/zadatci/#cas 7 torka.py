#cas 7 torka/tuple ne moze da se mijenja
a = (1,2,2)
print(type(a))
for i in a:
    print(i)
#a[1] = 9 #TypeError: 'tuple' object does not support item assignment
print(a.count(1)) # broji kolikose element iz zagrede ponavlja u torci
a = 2,3 #moze i bez zagrede, pythonski nacin je sa zagradama
print(type(a))
a = 1
print(type(a)) #klas je int !!!
#torka sa jednim elementom se ovako pise
a = 1,
print(a)
(c,d) = (5,7)
print(d)
print(c) # moze i ovako da se di

#setovi

a = {4,4,5,5} # ovo je skup ili ti set
print(a) #izbacuje sve duplikate
a.add(7)
print(a)
a.add(7) # ne dodaje zato sto vec postoji
print(a)
#print(a[2]) #TypeError: 'set' object is not subscriptable; neuredjeno i ne moze preko indeksa da se pristupi
a = set() #pravi prazan skup
print(type(a))
a.add(9) #dodaje u set
print(a)
print(type({5})) #<class 'set'>
c = {} # prazne {} su uvike rijecnici
print(type(c)) #<class 'dict'>

#rijecnik, dictonary


#rijecnik je struktura koja ima kljuc vrijednost!
dic = {"srb":"srbija"} # rijecnik mora sa ":" da se odvoja
print(type(dic))
print(dic)
opis_osobe = {"god":37,"ime":"Drazen","bracno stanje":1, "a":{"porodica":["mama","tata"]}}
print(opis_osobe["god"])# izbacuje 37; tj prekom kluca dolazis do vrijednosti!!!
print(opis_osobe)
opis_osobe["info"]=7 # dodaje novu vrijednost key je info
print(opis_osobe)
opis_osobe["god"] = 39 # mijenja godine na 39!
print(opis_osobe)
#ne mogu da se traze vrijendosti od nepostojeceg kljuca
#mora da se provjerava da li ima kljuc kako bi se mogao da promjeni
print(opis_osobe["a"]["porodica"][1])# pristup "a" pa dalje "porodici" pa dalje pozicija 1 (tata)

aa = {2,3,4}
bb = list(aa)
print(type(bb)) #lista
bb.append(3)
print(bb)
cc = set(bb) # posto je set sklanja duplikate
print(cc)
dd = (2,3,4)
print(id(dd))
print(type(dd)) #tuple
dd = list(dd)
print(id(dd)) # pravi novu memorijsku lokaciju
print(type(dd)) #lista