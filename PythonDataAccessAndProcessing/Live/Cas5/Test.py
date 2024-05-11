import random
import numpy as np
skup = set(random.randint(0,100) for i in range(20))
lista = list(skup)
lista.sort()
k = 5
lista1 = lista[0:k]
print(lista1)


dict = {i:random.randint(0,100) for i in range(20)}
print(dict)
keys = list(dict.keys())
print(keys)
values = list(dict.values())
print(values)
sorted_value = np.sort(values) #sortira po vrednostima [ 0  4  6 10 13 30 37 40 40 41 47 52 64 64 74 83 85 88 94 94]
print(sorted_value)
sorted_value_index = np.argsort(values) #sortira po indeksu [ 5 16 19  6 17 18  4 10  9  3 14 11  8  0  1  7 12 15 13  2]
print(sorted_value_index)

lista = [(3,5),(4,1),(7,4)]
print(max(lista)) #max gleda maksimum po prvoj koordinati!; izbacuje par gdje prva koordinata najveca --> (7,4)
print(max(lista)[1]) # vraca drugu kordinuta tamo gdje prva najveca --> 4
p = lambda kv: (kv[1], kv[0])
print(p((2,7)))