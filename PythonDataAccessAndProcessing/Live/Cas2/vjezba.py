lista = []
def linear_seq(sequence):
    for i in sequence:
        if isinstance(i, int):
            lista.append(i)
        else:
            linear_seq(i)
    return lista
 
sequence = [1,2,3,[4,5, (6,7)]]
 
print(linear_seq(sequence))
#[1,2,3,4,5,6,7]

a = 1
print(isinstance(a, int))

print(list(range(5)))
import numpy as np
print(list(np.arange(5)))

a = [2, 4, 6]
b = [1, 2, 3]
c = []
for i in range(len(a)):
    c.append((a[i],b[i]))
print(c)

d = [(a[i],b[i]) for i in range(len(a))]
print(d)
print(list(zip(a,b)))