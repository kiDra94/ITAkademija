x = 2 #inicjalizacija!
x = x +10
print(x)
x += 10
print(x)
x **=10
print(x)
print(12 & 10) #zbog poredjenje binarnih cifara rezultat bude 8; & == binarno I
print(12 | 10) #zbog poredjenje binarnih cifara rezultat bude 14; | == binarno ILI
print(12 ^ 10) #zbog poredjenje binarnih cifara rezultat bude 6; ^ == xor; ekskluzivno ili
print(12 >> 1) #pomjerna binarni kod u desno za n mjesta
print(12 << 3) #pomjerna binarni kod u lijevo za n mjesta
a = 12
print(a>>2)
print(a)    # print samo ispise kopije, vrijednost a ostaje ista
a >>= 2 #isto kao a = a >> 2
print(a)
a = False
if a==False:
    print("a je False 1")
if not a: # if a: poredi da li je a 1 tj TRUE, dakle if not a poredi da li je a 0 tj FALSE
    print("a je False 2")
if a==True:
    print("a je True 3")
if not a:
    print("a je True 4")
# logicki operator zadatak da li je a izmedju 5 i 10
a = int(input("Unesi broj: "))
if a > 5 and a <10:
    print("Broj",a,"je u rasponu izmedju 5 i 10")
else:
    print("Broj",a,"nije u rasponu izmedju 5 i 10")
'''
a = 2
if 5<a<10:
    print("Jeste")
else: 
    print("Nije") cudan nacin da se pise ali radi XD
'''
#lista 
a = [1,2,4]
print(id(a))
b = [1,2,4]
print(id(b))
if a==b:
    print("iste su")
else:
    print("nisu iste")
if a is b:
    print("iste memorijska lokacija") # nece se desiti zato sto a ima svoju a b svoju memoriju
b = a
if a is b:
    print("iste memorijska lokacija1") # prolazi zato sto b pokazuje na isto memorisko mjesto gdje je a
a[0] = 7
print(a) # [7, 2, 4] je rjesenje zato sto lokaciju 0 u ovom slucaju broj 1 promjeni
print(b) # dokaz da b i a pokazuju istu lokaciju
print(id(a))
print(id(b))
a = [2,3,4]
print(id(a)) # a je dobilo novu lokaciju
print(id(b)) # b je zadzalo staru lokaciju, tj prvobitnu od lokacije a
c = a + b
print(c) # [2, 3, 4, 7, 2, 4] u sustini samo spoji liste i pravi novu lokaciju
print(id(c))