#vjezba 2 ppf ex05 menu.py
prikaz_proizvoda   = 1
kupovina_proizvoda = 2
izlaz_iz_programa  = 3
ime_proizvoda      = "Samsung"
cijena_proizvoda   = 549
kolicina_novca     = int(input("Unesite kolicinu novca: "))
user_command       = int(input("Unesite komandu: "))
if user_command == prikaz_proizvoda:
    print("Ime: " + str(ime_proizvoda), "\n", "Cijena: " + str(cijena_proizvoda))
if user_command == kupovina_proizvoda:
    if cijena_proizvoda <= kolicina_novca:
        print("Kupili ste proizvod")
    else:
        print("Nemate dovoljno novca")
if user_command == izlaz_iz_programa:
    print("Dovidjenja!")
