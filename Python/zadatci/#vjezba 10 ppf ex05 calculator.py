#vjezba 10 ppf ex05 calculator.py
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
