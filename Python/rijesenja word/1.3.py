#Pomocu input funkcije unosimo vrednost sa standardnog ulaza
a=int(input("Unesite prvi ceo broj: "))   # vrsi se konverzija stringa u ceo broj. Unetu vrednost prebacujemo u ceo broj koriscenjem int funkcije 
b=int(input("Unesite drugi ceo broj: "))     # vrsi se konverzija stringa u ceo broj.  Unetu vrednost prebacujemo u ceo broj

#Realno deljenje 
kolicnik =a / b

#Celobrojno deljenje
div = a // b

#Stepenovanje broja a na stepen b
stepen = a ** b


print("Kolicnik {0:f}\nCelobrojni kolicnik {1:d}\nStepen {2:d}" .format(kolicnik ,div, stepen))

