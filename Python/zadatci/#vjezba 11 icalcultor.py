#vjezba 11 icalcultor.py
user_lang = str(input("Unesite jezik(en,de,srb): "))
guten_tag = "de"
good_day  = "en"
dobar_dan = "srb"
if user_lang == "de":
    broj1 = float(input("Geben Sie die erste Nummer ein: "))
    broj2 = float(input("Geben Sie die zweite Nummer ein "))
    operacija = input("Wählen Sie die Operation aus (add, sub, mul, div): ")
    if operacija == "add":
        rezultat = broj1+broj2
        print(f"Das Ergebniss ist: {rezultat:.2f}")
    elif operacija == "sub":
        rezultat = broj1-broj2
        print(f"Das Ergebniss ist: {rezultat:.2f}")
    elif operacija == "mul":
        rezultat = broj1*broj2
        print(f"Das Ergebniss ist: {rezultat:.2f}")
    elif operacija == "div":
        rezultat = broj1/broj2
        print(f"Das Ergebniss ist: {rezultat:.2f}")
    else: 
        print("Falsche Eingabe")
elif user_lang == "srb":
    broj1 = float(input("Unesite prvi broj: "))
    broj2 = float(input("Unesite drugi broj: "))
    operacija = input("Unesite operaciju (add, sub, mul, div): ")
    if operacija == "add":
        rezultat = broj1+broj2
        print(f"Rezultat je: {rezultat:.2f}")
    elif operacija == "sub":
        rezultat = broj1-broj2
        print(f"Rezultat je: {rezultat:.2f}")
    elif operacija == "mul":
        rezultat = broj1*broj2
        print(f"Rezultat je: {rezultat:.2f}")
    elif operacija == "div":
        rezultat = broj1/broj2
        print(f"Rezultat je: {rezultat:.2f}")
    else: 
        print("Pogresan unos!")
elif user_lang == "en":
    broj1 = float(input("Enter first number "))
    broj2 = float(input("Enter second nuber "))
    operacija = input("Chose operation (add, sub, mul, div): ")
    if operacija == "add":
        rezultat = broj1+broj2
        print(f"Result is: {rezultat:.2f}")
    elif operacija == "sub":
        rezultat = broj1-broj2
        print(f"Result is: {rezultat:.2f}")
    elif operacija == "mul":
        rezultat = broj1*broj2
        print(f"Result is: {rezultat:.2f}")
    elif operacija == "div":
        rezultat = broj1/broj2
        print(f"Result is: {rezultat:.2f}")
    else: 
        print("Wrong statement!")
