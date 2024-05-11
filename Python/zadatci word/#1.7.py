#1.7
a = int(input("Unesi a: "))
b = int(input("Unesi b: "))
if a > b:
    print("a {0} je veci od b {}".format(a,b))
elif a == b:
    print("a {} je jednak od b {}".format(a,b))
else: 
    print("a {} je manji od b {}".format(a,b))
if a != b:
    print("a {} je razlicit od b {}".format(a,b))