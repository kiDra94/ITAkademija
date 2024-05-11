import random

class intDict(object):
    """A dictionary with integer keys"""
    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
            
    def addEntry(self, dictKey, dictVal):
        """Assumes dictKey an int. Adds an entry."""
        hashBucket = self.buckets[dictKey%self.numBuckets] 
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return
        hashBucket.append((dictKey, dictVal))
        
    def getValue(self, dictKey):
        """Assumes dictKey an int. Returns entry associated
        with the key dictKey"""
        hashBucket = self.buckets[dictKey%self.numBuckets] # vrednost za kljuc dictKey traži se u redu sa indeksom dictKey%self.numBuckets
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None
    
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}' #result[:-1] omits the last comma

D = intDict(29)  # heš tabela ima 29 redova (numBuckets = 29)
for i in range(20): # u nju se unosi 20 vrednosti (0,1,...,19) za pseudoslučajne ključeve iz opsega (0,100000)
#choose a random int between 0 and 10**5
    key = random.randint(0, 10**5)
    D.addEntry(key, i)
print('The value of the intDict is:')
print(D)
print('\n', 'The buckets are:')
for hashBucket in D.buckets: #violates abstraction barrier
    print(' ', hashBucket)
    
kljuc = int(input("Unesi kljuc: "))    
while(kljuc!=-1):
    print(D.getValue(kljuc))
    kljuc = int(input("Unesi kljuc: ")) 