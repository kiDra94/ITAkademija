def saberi2():
    a=int(input("Unesite ceo broj: "))
    b=int(input("Unesite ceo broj: "))
    
    if a>=b:
        print("Greska, potrebno je da prvi broj bude striktno manji od drugog")
    else:
        s=0
        for i in range(a,b):
            s+=i
        print('Suma je: ',s)
        
saberi2()