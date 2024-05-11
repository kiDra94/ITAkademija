#1.14
troka = (1.3, 2.3, 2.1, 3.2, 4.4)
lista = list(troka)
lista[4] = 0
troka = tuple(lista)
print(troka)