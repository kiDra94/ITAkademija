stek=[]

while True:
    a=int(input("Unesite ceo broj: "))
    if(a==0):
        break
    stek.append(a)
    

print("Duzina steka je ",len(stek))

print("Izbaceni element je ",stek.pop())
print("Izbaceni element je ",stek.pop())
print("Izbaceni element je ",stek.pop())

print("Duzina steka je ",len(stek))
