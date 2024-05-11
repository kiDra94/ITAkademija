'''Zadatak 1.9. Napraviti nacrt koji prikazuje rast cene po godini. Početna cena je 50 I svake godine se povećava za 2.
 Prikazati porast cene od 2000 do 2021 godine.'''

#import modula
from matplotlib import pyplot as plt

#pravljenje liste x koja sadrzi godine od 2000-2022
x = []
for i in range(2000,2022):
     x.append(i)

#pravljenje liste y koja sadrzi vrednosti od 0-22 koja se povecavaju za 50
y=[]
c=50
for i in range(0,22):
     y.append(c+i)

#skiciranje grafika
plt.plot(x,y)

#ime labele za x
plt.xlabel("Godine")

#ime labele za y
plt.ylabel("Rast")

#ime celog grafika
plt.title("Rast po godini")

#prikazivanje grafika
plt.show()
