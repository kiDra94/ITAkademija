
#Modul za rad sa random metodama
import random

a=int(input("Unesite prvi broj: "))
b=int(input("Unesite drugi broj: "))

#Metoda randint vraca ceo random broj izmedju a i b gde su u izbor ukljuceni i a i b
c=random.randint(a,b)

print("Random broj je ",c)
