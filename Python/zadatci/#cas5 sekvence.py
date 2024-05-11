#cas5 sekvence
#stringovi
s = "sunce"
print(s.upper()) # upper stampa veliko, lower stampa mala slova
print(id(s))
s += "kisa"
print(s)
print(id(s)) #napravljena nova adresa!
print(s[0]) #je u ovom slucaju s od sunce
#s[0] = "A" #'str' object does not support item assignment;string je nemutabilan! ne mozes da promjenisvrijednost u stringovima
#liste
lista = [2,6,"Ana"] # u listama mogu biti razliciti tipovi!; najcesce se koristi isti radi manipulacije
print(lista)
lista[2] = 7
print(lista)
lista.remove(7) # brise tacno zadan element
print(lista)
lista[1] = 7
print(lista)
lista.append(4) # dodaje na kraju liste
print(lista)
lista.pop() #brise zadnji element
print(lista)
lista.pop(0) # brise element zadan u zagradi, tj na navedenoj poziciji
print(lista)
lista.append(4)
print(lista)
lista = [i for i in range(10)] # rezultal for i in range puni listu
print(lista)
lista.pop(4)
print(lista)
#zadatak: 2 liste; napraviti novu trecu koja ce da sadrzi prve 2 liste
lst1 = [1,3,5,7,9]
lst2 = [2,4,6,8]
lst3 = lst1 + lst2 # najlaksi nacin
lst4 =[]
for i in lst1:
    lst4.append(i)
for i in lst2:
    lst4.append(i)
print(lst3)
print(lst4)
lst3.sort() # u rastucem poretku
print(lst3)
lst3.reverse()
print(lst3)