a=int(input("Unesite prvi ceo broj:"))
b=int(input("Unesite drugi ceo broj: "))
c=int(input("Unesite treci ceo broj: "))

#Pretpostavljamo da je a maksimalni broj
max=a
#Ispitujemo da li promenljiva b ima vecu vrednost od maksimuma 
if(b>max):
    #Ako je uslov tacan vrednost promenljive b cuvamo u promenljivi max
    max=b
if(c>max):
    max=c
print("Maksimalni element je ",max)
