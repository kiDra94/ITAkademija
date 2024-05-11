a=int(input("Unesite prvi ceo broj: "))
b=int(input("Unesite drugi ceo broj: "))

if a<b:
    #Postavljamo b+1 kako bi se ispisala i vrednost promenljive b
    for i in range(a,b+1):
        print(i)
    else:
        print("ZAVRSENO")
    
else:
    print("Greska")
