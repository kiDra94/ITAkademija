def promena(s):
    #Razdvajanje stringa
    l=s.split('*')
    #Pretvaranje svih elemenata liste u cele brojeve
    l=list(map(int,l))
    
    #Mnozenje svih elemenata liste
    p=1
    for el in l:
        p=p*el
    return p
    
    
s='1*2*3*4'
p=promena(s)
print('Proizvod je ',p)
