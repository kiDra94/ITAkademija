import math

a=float(input("Unesite realni broj: "))
b=int(input("Unesite ceo broj: "))

#abs metoda vraca apsolutnu vrednost
aps_vrednost=abs(a)
#sqrt metoda vraca kvadratni koren broja
koren=math.sqrt(b)
#Metoda pow dize broj a na stepen b
stepen=pow(a,b)

print('Apsolutna vrednost broja {} je {:.2f}'.format(a,aps_vrednost))
print('Kvadratni koren broja {} je {:.2f}'.format(b,koren))
print('{}^{}={:.2f}'.format(a,b,stepen))