import sys

def objedini(a, b):
    c = []
    i = j = 0
    '''brojac ce sad uvijek zasigurno ici do kraja listi; zato sto smo dodali najvece brojeve na kraj liste!
    tek kad dodje do najduzeg broja onda dodaje oba u listu'''
    a.append(sys.maxsize) #dodaje na kraju liste najveci postujuci broj u pythonu
    b.append(sys.maxsize) #dodaje na kraju liste najveci postujuci broj u pythonu
    #print(a)
    #print(b)
    while i<len(a) and j<len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    return c[:-1] #vraca cijelu listu bez najduzeg broja koji smo dodali!!!


a = [1, 4, 5]
b = [2, 3, 7, 10, 50]
print(objedini(a,b))