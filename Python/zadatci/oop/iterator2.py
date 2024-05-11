import sys

class Counter:

    def __init__(self, start=0, stop=sys.maxsize):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            print("The maximal value is reached.")
            raise StopIteration
        else:
            self.start += 1
        return self.start


obj = Counter(41, 45)
for message in obj:  # petlja ide kroz iterabilni objekat
    print(message)

numbers = [2, 5, 8]  # iterable
iterator1 = iter(numbers)  # iterator
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))

# Ovo izaziva izuzetak StopIteration
'''  
obj = Counter(41, 45)
print(next(iter(obj)))
print(next(iter(obj)))
print(next(iter(obj)))
print(next(iter(obj)))
print(next(iter(obj)))
'''

obj = Counter(32)  # Ovo ide dva puta
print(next(iter(obj)))
print(next(iter(obj)))

'''
obj = Counter(41)  # Ovo ide do beskonačnosti
for message in obj:  # petlja ide kroz iterabilni objekat
    print(message)
'''

obj = Counter()  # Ovo počinje od 1
print(next(iter(obj)))
print(next(iter(obj)))

obj = Counter()
# for message in obj:  # petlja ide kroz iterabilni objekat
#   print(message)

obj = Counter(3, 30)
for message in obj:  # petlja ide kroz iterabilni objekat
    print(message)

obj = Counter(start=3, stop=10)
for message in obj:  # petlja ide kroz iterabilni objekat
    print(message)

obj = Counter(stop=10)
for message in obj:  # petlja ide kroz iterabilni objekat
    print(message)

obj = Counter(10, 12)
for message in obj:  # petlja ide kroz iterabilni objekat
    print(message)