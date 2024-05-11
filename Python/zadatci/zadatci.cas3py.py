#cas 3 pogledaj rijesenja!!!
#ppf-ex04 add.py
a = int(input("Unesi prvi broj: "))
b = int(input("Unesi drugi broj: "))
print("Zbir je: ", a + b)
#ppf-ex04 exchange.py
eur = 1.3
usd = 1.1
num = float(input("Unesite kolicinu novca: "))
total_euro = "Total EUR: %.2f" % (num/eur) # f oznacava float; 2 oznacava koliko decimala
total_dolar = "Total USD: %.2f" % (num/usd)
print("Total EUR: ", total_euro)
print("Total USD: ", total_dolar)
#ppf-ex04 tax.py
netto = float(input("Unesi cijenu: "))
porez = 0.2
print("Cijena sa porezom je: %.2f" % ((netto*porez)+netto))
##ppf-ex04 circlearea.py
poluprecnik = float(input("Unesi poluprecnik: "))
pi = 3.14
print("Povrsina kruga je: %.2f" % ((poluprecnik**2)*pi))
##ppf-ex04 change.py
kolicina = int(input("Unesite kolicinu: "))
tens = kolicina // 10                       #ovo nije elegantan nacin :D
fives   = (kolicina % 10) // 5              #fives = (kolicina-(tens*10)) // 5            
twos    = (kolicina % 10 % 5) // 2          #twos = (kolicina-(tens*10)-(fives*5)) // 2
ones    = (kolicina % 10 % 5 % 2) // 1      #ones = (kolicina-(tens*10)-(fives*5)-(twos*2)) // 1
print("Tens: ", tens)
print("Fives: ", fives)
print("Two's: ", twos)
print("Ones :" ,ones)
##ppf-ex04 even.py
a = int(input("Unesite broj: "))
if a%2 == 0:
    print("Broj je paran!")
else:
    print("Broj je neparan!")
###ppf-ex04 guess.py
import random
moj_broj = random.randint(1,10)
korisnicki_broj = int(input("Unesite broj od 1 do 10: "))
print("Broj od racunara: ", moj_broj)
if moj_broj == korisnicki_broj:
    print("Brojevi su jednaki: True")
else:
    print("Brojevi su jednaki: False")
###ppf-ex04 hit.py
proj_x   = 0
wall_x   = 7
proj_spd = 2
location = proj_x + proj_spd
if location>=wall_x:
    print("Hit: True")
else:
    print("Hit: False")
location += proj_spd
if location>=wall_x:
    print("Hit: True")
else:
    print("Hit: False")
location += proj_spd
if location>=wall_x:
    print("Hit: True")
else:
    print("Hit: False")
location += proj_spd
if location>=wall_x:
    print("Hit: True")
else:
    print("Hit: False")
##ppf-ex04 age.py
allowed_age = 13
age = int(input("Unesite starost: "))
if age>=allowed_age:
    print("Ulaz je dozvoljen")
else:
    print("Ulaz nije dozvoljen")
gender = input("Unesite pol:")
age = int(input("Unesite starost: "))
if gender == "musko" and age<18:
    print("Ulaz nije dozvoljen")
elif gender == "zensko" and age<16:
    print("Ulaz nije dozvoljen")
else:
    print("Ulaz je dozvoljen")
##ppf-ex04 login.py
db_username = "petar"
db_password = "123"
en_username = input("Unesite vase korisnicko ime: ")
en_password = input("Unesite vasu lozinku: ")
if db_username == en_username and db_password == en_password:
    print("True")
else:
    print("False")
#ppf-ex04 bbox.py
width  = 4
height = 8
x = int(input("Unesitie X: "))
y = int(input("Unesite Y: "))
if x<=width and y<=height:
    print("You are in the zone!")
else:
    print("You are not in the zone!")
user       = 1
admin      = 2
superadmin = 4
authorization_mask = admin | superadmin
user_role  = int(input("Enter role: "))
print("Allowed to access:", (authorization_mask & user_role) != 0)
#ppf-ex04 tank.py
dome =      1
tracks =    2
motor =     4
projectil = int(input("Enter hit zone: "))
if projectil == 1 or projectil == 2 or projectil == 4:
    pass
else:
    print("Pogresan unos!") #odgovor na pitanje!
criticalzone = tracks | motor
print("Tank cannot move:", (criticalzone & projectil) != 0)
#da li je ok sto kod npr broja 3 6 i 7 isto pokazuje true? 