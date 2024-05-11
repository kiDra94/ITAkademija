def ispitaj(l):
    l2=[]
    for a in l:
        if a%2==0:
            l2.append('Paran')
        else:
            l2.append('Neparan')
    return l2

lista1=[1,2,3,4,5]
lista2=ispitaj(lista1)
lista3=list(map(lambda x: 'Paran' if x%2==0 else 'Neparan',lista1))

print(lista1)
print(lista2)
print(lista3)