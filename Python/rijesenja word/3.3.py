#Prazna lista u kojoj cemo cuvati vrednosti
l=[]
#Beskonacna petlja
while(True):
    #Unos broja
    a=int(input("Unesite broj: "))
    #Ako se unese 0
    if(a==0):
        #Prekida se rad beskonacne petlje
        break
    #Inace se dodaje vrednost u listu
    l.append(a)

#Pravi se prazna lista u kojoj cemo dodavati elemente prebacene u string
l2=[]
for el in l:
    #Dodajemo u listu element prebacen u string 
    l2.append(str(el))

#Spajanje elemenata liste u string tako da se izmedju svakog elementa nalazi karakter *
s='*'.join(l2)

print(s)
