import sys

class Counter:

    def __init__(self, start=0, stop=sys.maxsize):
        self.start = start
        self.stop = stop

    def get(self):
        return self.start

    def increment(self):
        if self.start >= self.stop:
            print("The maximal value is reached.")
            #raise StopIteration # kad predje vrijednost prekida program
        else:
            self.start += 1
        return self.start


c = Counter(10, 12)
print(c.get())
c.increment()
print(c.get())
c.increment()
print(c.get())
c.increment()
c.increment()
print(c.get())

'''obj = Counter(27,30) # objekat nema __iter__ metodu i nije iterabilan
for message in obj:  # TypeError: 'Counter' object is not iterable
    obj.increment()
    print(obj.get())'''