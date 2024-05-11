def f(a=5,b=0,c=9):
    print(a,b,c)

f(1,2,3)
f(1,2)
f(1)
f()

def g(*args):
    print(args)

g(1,2,3,4,5)
g(1,2,3,4,5,7,8,9,0)

def h(a,b,*c,**k):
    print(a,b,c,k["s"],k["s2"]) # print(a,b,c,k) ovako ispisuje ceo recnik k

h(3,4,7,9,2,s="Dobar dan",s2="Dobro vece")

def Min(a: int,b: int) -> int:
    return a if a<b else b

c = min(7,9)
print(c)
print(Min(7,9))

def kako_hocemo(*a: int) -> int:
    #print(type(a))
    m = a[0] # m = 3
    for i in range(1,len(a)):
        if a[i] > m:
            m = a[i]
    return m
  

maxi = kako_hocemo(3,6,7,1,2,0,9,8,21)
print(maxi)

import sys

def kako_hocemo2(*a: int) -> int:
    m = -sys.maxsize - 1
    for i in a:
        if i > m:
            m = i
    return m
  

maxi = kako_hocemo2(-4,-7)
print(maxi)

def suma(*args: int) -> int:
    s: int = 0
    for i in args:
        s += i
    return s

print(suma(93,2,5,6,8,9,1,9))

def suma_n(n: int) -> int :
    s = 0
    for i in range(1,n+1):
        s += i
    return s

print(suma_n(5))
print(suma_n(100))

def f(n):
    if n==0:
        return #bez ovog if-a bi program pukao posot ne bi imao kraja! return se u def funkcijima koristi kao break
    print(n,end=" ")
    f(n-1)
    print(n,end=" ") #rekurzija; spisuje brojeva "unazad" zato sto se ovo tek krece desavati kad f(n-1) zavrsi; uvijek ispisuje korak po korak nazad!!

f(3)

def kako_hocemo3(*a: int) -> int:
    m = a[0]
    for i in a[1:]:
        if i > m:
            m = i
    return m

maxi = kako_hocemo3(-4,-7,2)
print(maxi)

a = [1,2,3,4,5]
def parcici(a):
    if len(a)==0:
        return
    print(a)
    parcici(a[1:])

parcici(a)

a = [1,2,3,4,5]
def itertivno_parcici(a):
   for i in range(len(a)):
       print(a[i:])

itertivno_parcici(a)

def suma_rekurzija(n):
    if n == 0:
        return 0 #raucna 0 umjesto 0 + (0-1); tj raacuna 0+0
    return n + suma_rekurzija(n-1)

print(suma_rekurzija(5))

def rek_suma(n):
    print(f"Poziva se rek_sima ({n})")
    if n==0:
        return 0
    return n + rek_suma(n-1)
 
print(rek_suma(5))
 
def sum_number(a, b):
    return a + b
 
print(sum_number(1, 3))
 
sum_number_l = lambda a, b: a + b
print(sum_number_l(1, 3))
 
def myfunction(f):
    f("Hello World!")
 
myfunction(print)
 
def myfunction2(f):
    return f("Hello World!")
 
print(myfunction2(len))
 
def moja(s):
    return s[6]
 
print(myfunction2(moja))

str1 = 'GeeksforGeeks'
 
upper = lambda string: string.upper()
print(upper(str1))
 
def u_velika(s):
    return s.upper()
 
print(u_velika(str1))
 
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
for item in is_even_list:
	print(item())

def unos():
    lst = []
    k = int(input("Unesi broj "))
    while(k!=0):
        lst.append(k)
        k = int(input("Unesi broj "))
    return lst

def sortiraj(lst):
    lst.sort(reverse=True)
    return lst

def ispis(lst):
    print("Lista je: ",end="")
    for i in lst:
        print(i,end=" ")


'''lista = unos()
lista = sortiraj(lista)
ispis(lista)'''

ispis(sortiraj(unos()))

