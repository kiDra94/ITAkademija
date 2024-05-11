from Objedini2 import objedini
import random

def merge_sort(a):
    if len(a) == 1:
        return a
    return objedini(merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:]))

print(merge_sort([5, 2, 4, 7, 1, 3, 2, 6]))

a = [random.randint(0,100) for i in range(100)]
print(merge_sort(a))
