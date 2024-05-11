#vjezba 0 ppfex05 odds.py
match = input("Unesi utakmicu: ")
kvota1 = input("Unesi kvotu za domacina: ")
if(not kvota1.replace(".","").isnumeric()):
    print("Sorry home tip is not numeric")
    exit(0)
if float(kvota1)<1:
    print("Kovota ne moze da bude manja od 1")
    exit(0)
kvota2 = input("Unesi kvotu za nerjeseno: ")
if(not kvota2.replace(".","").isnumeric()):
    print("Sorry home tip is not numeric")
    exit(0)
if float(kvota2)<1:
    print("Kovota ne moze da bude manja od 1")
    exit(0)
kvota3 = input("Unesi kvotu za gosta: ")
if(not kvota3.replace(".","").isnumeric()):
    print("Sorry home tip is not numeric")
    exit(0)
if float(kvota3)<1:
    print("Kovota ne moze da bude manja od 1")
    exit(0)
print("Thank you, your odd is: ")
print("Match: ", match)
print("Home: ", kvota1)
print("Draw: ", kvota2)
print("Away: ", kvota3)
