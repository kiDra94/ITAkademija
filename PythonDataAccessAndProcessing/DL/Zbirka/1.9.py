'''Zadatak 1.9. Napraviti nacrt koji prikazuje rast cene po godini. Početna cena je 50 I svake godine se povećava za 2.
 Prikazati porast cene od 2000 do 2021 godine.'''


from matplotlib import pyplot as plt

x = []
for i in range(2000,2022):
     x.append(i)
y=[]
c=50
for i in range(0,22):
     y.append(c+i)
plt.plot(x,y)
plt.xlabel("Godine")
plt.ylabel("Rast")
plt.title("Rast po godini")
plt.show()
