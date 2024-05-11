'''kor_ime = "mika"
lozinka = "loz"
if lozinka == "loz" and kor_ime == "mika":
    print("Uspjesna prijava")
else:
    print("Neuspesna prijava")

if kor_ime == "mika":
    if lozinka == "loz":
        print("Uspjesna prijava")
    else:
        print("Provjeri lozinku")
else:
    print("Provjeri korisnicko ime")'''
#zadatak da li se moze napraviti trougao, zbir 2 manje ne smije da bude duzi od najvece
'''a = 3
b = 4
c = 5
if a+b > c and b+c > a and a+c > b:
    print("Trougao postoji!")
else:
    print("Trougao ne postoji!")'''
#odedi minimum 3 broja
'''a = 7.5
b = 4.4
c = 2.1
if(a<b):
    if(a<c):
        minimum = a
    else:
        minimum = c
else:
    if(b<c):
        minimum = b
    else:
        minimum = c
print(minimum)
print(min(a,b,c)) #moze i da s ekoristi funkcija min u pythonu; tj. postoji ta ugradjena funkcija'''
'''
my_operation = "read" 
if my_operation == "read": 
    print("perform read operation…") 
elif my_operation == "update": 
    print("perform update operation …") 
elif my_operation == "insert": 
    print("perform insert operation …") 
elif my_operation == "delete": 
    print ("perform delete operation …") 
else: 
    print("wrong variant if operation !!! ")
 # verzija 3.10 i vise postoji mogucnost match case; preglednije nema elif-ova, manje za kucati
my_operation = "read" 
match my_operation: 
    case "read": 
        print("perform read operation…") 
    case "update": 
        print("perform update operation …") 
    case "insert": 
        print("perform insert operation …") 
    case "delete": 
        print("perform delete operation …") 
    case _: #donja crta znaci da ako nista ne ispunjava
        print("wrong variant if operation !!!")'''
#petlje
'''print("Zdravo")
print("Zdravo")
print("Zdravo")
print("Zdravo")
print("Zdravo")
print("Zdravo")
print("Zdravo")
print("Zdravo")
print("Zdravo")
print("Zdravo")

for i in range(100): #range pokazuje koliko puta da se ponovi nesto, range je ugradjena python funckija; i == incremented
    print("Zdravo")
for i in range(8,10): #ispise 2 puta ;8 jednom i 9 jednom, uvijek ide do broja koje se unese a pocinje od 0, osim ako ne ukucamo nesto
    print("Zdravo")
for i in range(0,10):
    print("Zdravo " + str(i)) #ispise zdravo 0 do zdravo 10'''
'''
suma = 0
for i in range(1,11):
    suma += i # ovo je kumulativni rast
    print("brojac i je " + str(i) + " suma je " + str(suma))
print("brojac i je na kraju " + str(i))
#faktorijal od 5 je 5*4*3*2*1,
prod = 1 # kad se mnozi uvjek se sa 1 pocinje, kad mnozi s 0 onda je proizvod uvijek 0
for i in range(1,11):
    prod *= i # ovo je kumulativni rast
    print("brojac i je " + str(i) + " Proizvod je " + str(prod))
print("brojac i je na kraju " + str(i))
# sumiranje samo parnih brojeva
suma = 0
for i in range(0,11):
    if i%2==0:
        suma += i
print(suma)
# sumiranje samo neparnih brojeva
suma = 0
for i in range(0,11):
    if i%2==1:
        suma += i
print(suma)
#kraci nacin da se spoje if i for!!!
suma = 0
for i in range(0,11,2): #2 oznacava kako da skace(zove se !korak!); kad se stavi 2 skace 0/2/4/6 itd dok ne doje do zadnjeg broja
        suma += i
print(suma)
suma = 0
for i in range(0,11):
    if i%2==0:
        suma += i
print(suma) !!!kod iznad je isti kao ovaj, mnogo kraci!!!
#jos oblika
for i in [3,14,15,6,77]: # ne ide kroz range; nego kroz listu
     if i>=10:
          print(i, end=" ") #sa end= definisemo seperator; u ovom slucaj je to prazno mjesto(space)

lista = [i for i in range(0,5)] #list comprehantion!, pravi listu definsan po operaciji u [];moze biti i slozenije sa if
print(lista)
print(lista[2:4]) # cita se od 2 do 4; zove se slajsovanje; uslov je da je lista definisana; prikazuje samo definisano
'''
#zadatak da ispise 3 zijezde pa 3 zvijezde pa 3 zvijezde
for i in range(9):
     print("*", end=" ") #ispise u liniji
for i in range(10):     #sa ovom funkcije kad ispusije poslije 3 skace u novi red
     print("*", end=" ")
     if i%3==0:
         print("\n")
print() #stampa prazno mjesto tj nista
n = 10
for i in range(1,n*n+1): #n*n+1 da bi obuhvatio i n*n!
     print("*",end=" ")
     if i%n==0:
          print("\n") #moze i print()
#vjezba ppf-ex06 treba da se koriste break i countinue
for i in range(1,n):
     if(i==5):
          break #prekida i ne pise dalje
     print(i)
for i in range(1,n):
     if(i==5):
          continue #preskace, tj ne pise 5 u ovom slucaju
     print(i)
for i in range(1,n):
     if(i>5 and i<8): #nece ispisati 6 i 7
          continue 
     print(i)
print("novi red")
for i in range(0,24): #i uzme 0 j uzme 0; i sve dok j ne dodje do 59 i ostaje 0; ispisan je u sustini sat; ukupan broj interakcija je 24*60!!!
     for j in range(0,60):
          print(str(i)+ " " + str(j))