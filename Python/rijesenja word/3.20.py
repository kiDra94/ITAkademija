

string='Pera Peric ima 36 godina i zivi u ulici Ohridska 53/96'

br=''
for c in string:
    #Metoda isdigit proverava da li su svi karakteri stringa cifre. Ako jesu vraca True a ako nisu vraca False.
    if c.isdigit():
        br+=c
        
print(br)