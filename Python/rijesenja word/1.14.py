

t=(1.1,2.2,3.3,4.4,5.5)

#Ako bismo pokusali da izmenimo element torke  t[4]=0 dobili bismo gresku, jer je torka nepromenljiv tip. 
#Zato moramo da je prebacimo u listu, pa onda izmenimo element i da je vratimo u torku

l=list(t)  #Funkcija list prebacuje element u listu
l[4]=0 #Izmena vrednosti poslednjeg elementa
t=tuple(l) #Funkcija tuple prebacuje element u torku
print(t)
