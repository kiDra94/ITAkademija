

with open('brojevi.txt','r') as ulaz:
    podaci=ulaz.read()
    
with open('cifre.txt','w') as izlaz:
    lista=podaci.split(",")
    print(lista)
    lista=list(map(int,lista))
    for broj in lista:
        s=0
        broj2=broj
        while broj2>0:
            s=s+broj2%10
            broj2=broj2//10
        print(s)
            
        if s%2==0:
            ispis=str(broj) + ' '
            izlaz.write(ispis)
        
