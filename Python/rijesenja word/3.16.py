lista=[('zuta', 1), ('plava', 2), ('zuta', 3), ('plava', 4), ('crvena', 5), ('zelena',6)]

recnik={}

for el in lista:
    if el[0] in recnik.keys():
        recnik[el[0]].append(el[1])
    else:
        recnik[el[0]]=[el[1]]        
        
        
print(recnik)