def spajanje(l):
    samoglasnici_lista=[]
    for el in l:
        if (el=='a' or el=='e' or el=='i' or el=='o' or el=='u') and (el not in samoglasnici_lista):
            samoglasnici_lista.append(el)
    
    samoglasnici='_'.join(samoglasnici_lista)
    return samoglasnici

lista=['a','b','e','u','s','h','a','e','i']
print(spajanje(lista))
    
