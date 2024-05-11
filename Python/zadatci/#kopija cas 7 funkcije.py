#kopija cas 7 funkcije
a = 3
b = 4
c = a + b
print(c)

a : int = 3
b : int = 4
c : int = a + b
print(c)

def ispis():
    print("Ovo je za pocetak.")
    print("Ovo je za pocetak.")

def zbir():
    a : int = 3
    b : int = 4
    c : int = a + b
    print(c)

def zbir2(a,b):
    c = a + b
    print(c)

def zbir3(a,b):
    c = a + b
    return c

zbir()
zbir2(10,15)

#zbir2(int(input("Unesi prvi broj ")),int(input("Unesi drugi broj ")))
d = zbir3(10,15)
print(d)
print(zbir3(10,15))

def zbir4(a: int,b: int) -> int:
    c: int = a + b
    return c

def zbir5(a: int,b: int) -> int:
    return a + b

def zbir6(a: int = 9,b: int = 7) -> int:
    return a + b

def zbir6(*a):
    for i in a:
        print(i,end=" ")

print(zbir6(1,2)) 
print(zbir6(1)) 
print(zbir6())
zbir6(4,4,5,6,7,8,2,1,1,1)

def max_3_broja(a: float, b: float, c: float) -> float:
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
print(max_3_broja(7,78,56))

def suma(n: int) -> int:
    s = 0
    for i in range(1,n+1):
        s+=i
    return s

print(suma(100))
a = suma(10000000)
print(a)

def fun1():
    print("Ja sam prva fun")

def fun2():
    print("Ja sam druga fun")
    fun1()

def fun3():
    print("Ja sam treca fun")
    fun2()
    fun1()

fun3()

def f(n):
    if n==0:
        return
    print("Nema kraja",n)
    f(n-1)

f(5)