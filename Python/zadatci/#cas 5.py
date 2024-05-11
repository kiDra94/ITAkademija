#cas 5 
#petlje krece od vjezbe 4
#vjezba 4 ppf ex06
'''h = 10
for i in range(h):
    for j in range(h):
        print("*", end="")
    print() #unutrasnja skace u novi red posto se zavrsila; blok unutrasnje petlje je iskljucivo print("*", end="")
             #blok spoljasnje su for j ... i print()
# ovo iznad stampa pravougaonik
#vjezba 4
h = 10
for i in range(h):
    for j in range(i+1): # i+1 da ne pise prazno mjesto!
        print("*", end="")
    print()
#isti zadatak sa jednom petljom! moze kad je input str!
h = 10
s = "*"
for i in range(1,h+1):
    print(i*s, end="") # za trougao; za kvadrat je h*s
    print()
#vjezba 5
h = 10
x = 1
for i in range(2*h):
    for j in range(x):
        print("*", end="")
    x = x + 1 if i < h-1 else x - 1
    print()
h = 10 # nije petlja u petlji; nego petlja do petlja
s = "*"
for i in range(1,h):
    print(i*s) 
for j in range(h,0,-1): #-1 znaci da preskace po jedan korak kad pise
    print(j*s)
# while petlja se koristi kad ne znas dokle ides; nego cekas uslov:
#zadatak 
#while mora da ima pocetnu vrijednost prije pokretanja petlje
n = 10
i = 0 # brojac
while i<10: # ti govoris dokle se povecava brojac i; opasnot moze da ide u beskonacnost;
    print(i)
    i += 1 # uvecava i kako bi prekinuo petlju; npr da ovoga nema program bi se vrtio u beskonacnost
print(i) # ovdje ispisuje 10 zato sto je i stigao do 10, ali ne upada u petlju!
#od 1 do 10
n = 10
i = 0
while i<10:
    i += 1
    print(i)
#parni
n = 10
i = 0
while i<10:
    i += 2
    print(i)
#neparni
n = 10
i = 1 #jedno rijesenje je sa i=-1 i ista petlja kao parni; ovo ispod je elegantnije rijesenje
while i<10:
    print(i)
    i += 2
#za while petlji vazi brejk i countinue istoa kao i za for petlje
# sve neparne sem broja 3 od 1 do 10
n = 10
i = -1
k = 3 #broj koji treba da se preskoci
while i<n-1:
    i += 2
    if i==k:
        continue #ne smije da bude zadnji posto prekida petlju
    print(i)
n = 10
i = -1
k = 3 #broj koji treba da se preskoci
while i<n-1:
    i += 2
    if i==k:
        break #prekida petlju
    print(i)
#suma prvih 10 brojeva
i = 0
suma = 0 
while i<11:
    suma += i
print("Suma je: ", suma, "Brojac je: ", i)
suma = 0
for i in range (0,11):
    suma+=i
print(suma)
# suma parnih brojeva
i = 0
suma = 0 
while i<11:
    suma += i
    i += 2
print("Suma je: ", suma)
suma = 0
for i in range (0,11,2):
    suma+=i
print(suma)
# da ispise # ## ### #### na vise nacina bilo pitanje 
s=""
for i in range(1,5):
    s+="#"
    print(s,end=" ")
    
print()
for i in range(1,5):
    for j in range(0,i):
        print("#",end="")
    print(" ",end="")
# nastavak while petlje crtanje duplog trougla; kombinacija while i for petlje
n = 10
i = znak = 1
while(i>0):
    for j in range(0,i):
        print("*",end="")
    if(i==n):
        znak-=2 # kad i dodje do 10 znak se smanji na -1 i ostaje takav, sto znaci da se i posljie stalno smanjuje za 1!!!
    i+=znak
    print()
n = 10
i = znak = 1
while(i>0):
    for j in range(0,i):
        print("*",end="")
    if(i==n):
        znak*=-1 # u ovom slucaj je 1*(-1) sto znaci da je i == -1; opet se smanjuje poslije kao u gornjem slucaju; zove se cesto indikator
    i+=znak
    print()
import time
target  = 20
x       = 1
dir     = 1
while True:
    print("\r",end="")
    j = 0
    while j < target:
        print("#" if x==j else " ",end="")
        j+=1
    if x==0 or x==target:
        dir*=-1
    x+=dir
    time.sleep(0.1)
#zadatak da se nacrta okvir sa X 
n = 10 
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*" if i==1 or j==1 or i==n or j==n or i==j or i+j==n+1 else " ", end="") #i==n-j-1 or j ==n-i-1 moj kod, korisven je laksi i prakticnijji
    print()'''