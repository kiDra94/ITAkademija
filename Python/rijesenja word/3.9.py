red=[]

while True:
    a=input("Unesite karakter: ")
    if(a=='A'):
        break
    red.append(a)
    

print("Duzina reda je ",len(red))

print("Izbaceni element je ",red.pop(0))
print("Izbaceni element je ",red.pop(0))
print("Izbaceni element je ",red.pop(0))

print("Duzina reda je ",len(red))

