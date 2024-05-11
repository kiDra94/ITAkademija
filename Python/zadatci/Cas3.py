a = "33"
b = int(a)
print(type(a))
print(type(b))
#a = int("3c") ne moze zato sto int moze samo da bude cijeli broj ValueError: invalid literal for int() with base 10: '3c'
print(3/2)
print(int(3/2)) # pokaze 1, zato sto ima 1 cijeli dio
print(3//2) # // dijeli na cijeli broj
print(2*5) #mnozenje
print(2**5) #** na petu; stepenovanje!
print("2"*5) #ispise 5 puta broj 2 zato sto je 2 u ovom slucaju string
print(2**1000)
c = 4/2
print(type(c))
print(c)
print(2+3-1*4/2) # drzi se matematickih pravila; prvo mnozenje i djeljenje
print((2+3-1)*4/2) #koristiti zagrade
print(10//3) # djeljenje bez ostatka
print(10%3) # Cjelobrojni ostatak od djeljenja
print(2**3) # stepenovanje
#zadatak, provjera da li je broj paran
broj = int(input("Unesi broj: "))
if(broj%2==0):  # if broj%2==0: isto funkcionise
    print("Broj",broj,"je paran") # moze i  print("Broj" + str(broj) + "je paran")
else: 
    print("Broj",broj,"je neparan") # moze i print("Broj je %d neparan" % broj) ili print(f"Broj je {broj} neparan")
print(f"Broj je {broj} neparan") #formatiran string; izmedju {} je mutabilni dio/dinamicki

import math #importuje math funkcije, normalno ide na pocetak
print(math.sqrt(7)) # sqrt. je korenovanje
print(round(math.sqrt(7),2)) # ,2 zaokruzuje na 2 decimale!

