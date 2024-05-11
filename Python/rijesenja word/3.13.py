
povrce={
    'Paradajz':150.5,
    'Krastavac':100.45,
    'Krompir':250.89
    }


novo_povrce=input("Unesite ime povrca: ")

if novo_povrce not in povrce.keys():
    cena=float(input("Unesite cenu " + novo_povrce + 'a: '))
    
    #dodavanja novog para u recnik
    povrce[novo_povrce]=cena
else:
    print(novo_povrce + ' se vec nalazi u recniku')
    
s=0
for kljuc in povrce:
    s=s+povrce[kljuc]
    
print("Suma za placanje je : ",s)
