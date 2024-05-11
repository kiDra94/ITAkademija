a=int(input("Unesite ceo broj: "))

if (a<=0):
    print("Broj je negativan ili nula")
elif(a>0 and a<10):
    print("Broj je jednocifren")
elif(a>=10 and a<100):
    print("Broj je dvocifren")
else:   
    print("Broj je trocifren ili veći")
