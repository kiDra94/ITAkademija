#dodavanja elementa na prvo mjesto!!!
niz = [13,5,7]
niz.append(17)
for i in range(len(niz)-1,0,-1):
    niz[i] = niz[i-1]
niz[0] = 4
print(niz)