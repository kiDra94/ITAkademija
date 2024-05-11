def linear_seq(sequence, lista):
    for i in sequence:
        if isinstance(i, int):
            lista.append(i)
        else:
            linear_seq(i, lista)
    return lista

sequence = [1,2,3,[4,5, (6,7)]]

print(linear_seq(sequence, []))
print("------------------")

import numpy as np

# create a 3x2 array
an_array = np.array([[11,12], [21, 22], [31, 32]])
filtered = an_array
print(an_array)

filter = (an_array > 15)
print(filter)
print(an_array[filter])
print("------------------")
c = []
for i in an_array:
    for j in i:
        if j > 15:
            c.append(j)
print(c)
print("------------------")
print([j for i in an_array for j in i if j>15])
from random import randint
print([[randint(0,10) for j in range(4)] for i in range(5)])
print("------------------")
class Neka:
    pass

print(type(Neka))

array = np.array([1,2,1,4,2,1,4,2])

print(np.unique(array))

nova = []
for i in [1,2,1,4,2,1,4,2]:
    if i not in nova:
        nova.append(i)

print(nova)
a = [1,2,1,4,2,1,4,2]
print({i for i in a})