#Definisanje liste
l=[5,6,3,9]

#Ispis 3. elementa liste, on se nalazi na 2. indeksu
print(l[2])

#Ispis elemenata od indeksa 1 do indeksa 3 (element na indeksu 3 se nece uzeti u obzir)
print(l[1:3])

#izbacivanje elementa na poziciji 2
l.pop(2)
print(l)

#Obrtanje liste
l.reverse()
print(l)
