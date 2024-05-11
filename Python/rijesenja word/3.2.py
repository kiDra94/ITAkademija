s1=input("Unesite prvi string: ")
s2=input("Unesite drugi string: ")

#Proveravanje duzine stringova
if(len(s1)<6 or len(s2)<6):
    print("GRESKA")
else:
    #Izdvajanje podstringova
    s1_isecak=s1[3:6]
    s2_isecak=s2[3:6]
    #Ispitivanje jednakosti podstringova
    if(s1_isecak==s2_isecak):
        print("DA")
    else:
        print("NE")
