a=int(input("Unesite prvi ceo broj: "))
b=int(input("Unesite drugi ceo broj: "))

if(a<b):
    print("Minimalni element je ",a)
elif(b<a):
    print("Minimalni element je ",b)
else:
    print("a i b imaju iste vrednosti")
