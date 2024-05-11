#cas 6 21.11 nastavak liste
#list = [] ; treba izbjegavati, posto je list kljucna rijec 
lista = []
print(lista)
lista.append(1)
print(lista)
lista2 = [3,4]
lista.extend(lista2) # prosiri lista sa elementima iz lista2
print(lista)
lista.insert(1,7)
print(lista.append(7))
print(lista)
print(lista.count(7)) # count broji koliko puta se nesto ponavlja u listi
print(lista.pop(3)) # pop brise za pozicije
print(lista)
lista.clear()
print(lista)
lista = [3,6,2,7,7,9,9]
for i in lista: #ispisuje listu jedan po jedan element
    print(i, end=" ")
lista[3]=45 # na trecoj poziciji dodaje novi elemnt, stara vrijednost se brise
print("\n",lista) #ispis u novi red
print("---------------")
#mijenja pozicije
a = 7
b = 5
print(a,b)
a,b = b,a 
print(a,b)

a = 7
b = 5
pom = a
a = b
b = pom
print(a,b)

a = 7
b = 5
a = a - b # a = 2 b = 5
b = a + b # a = 2 b = 7
a = b - a # a = 5 b = 7
print(a,b)

lista = [3,6,2,7,7,9,9]
#zamjena 1 i 3 pozicija liste preko 3 naredbe
pom = lista[1] # pom 6
lista[1] = lista[3]
lista[3] = pom
print(lista)
#zamjena 1 i 3 poslije na brzi nacin
lista[1],lista[3] = lista[3],lista[1]
print(lista)
# sortiranje liste
lista.sort()
print(lista)
#okretanje
lista.reverse()
print(lista)

#algoritam za sortiranje nizova
#rastuci poredak
lista = [7,2,1,5,4,3]
for i in range(len(lista)-1): #i-1 posto nema potrebe da se poredi zadnji sa zadnjim, tj sam sa sobom, manje posla za program
    for j in range(i+1, len(lista)):#i+1 da ne krece od 0 posto nije potrebno da poredi sam sa sobom
        if lista[i] > lista[j]:
            (lista[i],lista[j]) = (lista[j],lista[i])
print(lista)

#opadajuci poredak poredak
lista = [7,2,1,5,4,3]
for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        if lista[i] < lista[j]:
            (lista[i],lista[j])=(lista[j],lista[i])
print(lista)
print("---------------")
lista=[5,9,2,5,4,7,7]
print(lista[2:5]) #uzimanje parce liste od 2 do 5 indexa; posljednji se ne racuna kao kod range
print(lista[:5]) # ako se prvi ne navede ide od 0
print(lista[3:]) # krece od 3 indeksa i ide do kraja
print(lista[1:6:2]) # krece od 1 do 6(bez njega) i skace po 2
print(lista[::]) # cijela lista kad nema ogranicenja
print(lista[:]) # kad se ne stavi korak podrazumjeva se korak 1
''' #posljednja pozicija se isto oznacava sa -1 u pythonu
#indeksi mogu da idu od 0 pa navise, sa lijeva na desno
#li od -1 pa na nize sa desna na lijevo'''

print(lista[2:5])
print(lista[-5:-2])
print(lista[:-2]) #krece od 0 do -2
print(lista[-2:]) # krece od -2 i ide do kraja
print(lista[::-1]) # listas ide unazad; posto ineks ide od -1
print(lista[2:5:-1]) #vraca prazan niz posto ide u nazad
print(lista[2::-1]) #krece od pozicije 2 i ide do pocetka liste
print(lista[4:1:-1])# krece od indeks 4 ide do 1
print(lista[-3:-6:-1])#isto kao gore
lista = [3,4,5,7,9,20]
print(lista[2:5][:2]) #ispisuje prva 2 elemente u slice od[2:5]
print(lista[:5][2]) #od 0 do 4 i uzima samo 2 poziciju posto u drugoj [] nema dvitacki
print(lista[1:5][2]) #ovdje uzima broj 7 zato sto u slice pozicije opet od 0 krecu
#del lista[:] #brise sve elemnte'''

a = [1,2,3]
b = [4,5,6]
c = []
for i in range(len(a)):
    c.append(a[i]+b[i])
# c = [a[i]+b[i] for i in range(len(a))] #radi isto kao ovo iznad
print(c)
print("---------------")
# sortirati parne i neaprne u 2 liste na vise nacina
lista = [i for i in range(1,10)] # i unutar zagrade se tertira kao append
print(lista)
lst_neparni = []
lst_parni   = []
for x in lista:
    if x % 2 == 0:
        lst_parni.append(x)
    else:
        lst_neparni.append(x)
print(lst_neparni)
print(lst_parni)
# skracenija varijanta
lista = [i for i in range(1,10)]
lst_neparni = []
lst_parni   = []
for x in lista:
    lst_parni.append(x) if x%2 == 0 else lst_neparni.append(x)
print(lst_neparni)
print(lst_parni)
# preko lst comprehantion ne mora se praviti prazna lista; pythonski nacin, ternarni operator
lista = [i for i in range(1,10)]
lst_parni1     = [x for x in lista if x%2 == 0]
lst_neparni1   = [x for x in lista if x%2] # x%2 znaci da je razlicito od 0; isto x%2 != 0 ili x%2 == 1
print(lst_neparni1)
print(lst_parni1)
print("---------------")
# 2 petlje i list comprehantion
lista_od_dvije_petlje = [(i,j) for i in range(3) for j in range(3)] #prva petlja je spoljasnja druga je unutrasnja
print(lista_od_dvije_petlje)
#moze da se kombinuje i sa ifom
lista_od_dvije_petlje = [(i,j) for i in range(3) for j in range(3) if j > i]
print(lista_od_dvije_petlje)
#standardan nacin; ovo gore je pythonski
lista_od_dvije_petlje = []
if i in range(3):
    for j in range(3):
        if j>i:
            lista_od_dvije_petlje.append((i,j))
print("---------------")
#anavolimilovana palindrom
s = "AnavoliMilovana"
s = s.lower() #sve pretvara u mala slova ince bi bila razlika izmedju A i a
print("Jeste palindrom" if s[::-1] == s[::] else "Nije palindrom") # sliceovi rade kod stringova
#sta se desava u pozadini!
for i in range(len(s)//2): #len je duzina // da bude vrijednost int!!
    if (s[i]!=s[len(s)-1-i]): # bolje je != posto ako prvi nije isti odma ne ispunjava uslov, tako da program manje radi
        print("NIJE PALINDROM")
        break
else: #else mora biti van if petlje posto se u ovom slucaju tek desava kad petlja zavrsi!
    print("JESTE PALINDROM")





