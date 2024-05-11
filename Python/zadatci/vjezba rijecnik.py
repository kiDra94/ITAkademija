#rijenik:
rijecnik = {"it":"Benvenuti", "de":"Guten Tag", "en":"Good day"}
unos = str(input("Choose leangueg (it/de/en): "))
poruka = rijecnik.get(unos, "Nepoznat jezik")
print(poruka)