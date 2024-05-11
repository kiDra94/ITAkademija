#cas 7 funkcije
# ovo je program za sabiranje 2 broja
a = 3
b = 4
c = a + b
print(c)

a : int = 3
b : int = 4 
c : int = a + b
#izmedju ova 2 koda nema sustinske razlike, ali kod 2 tacno definise promjenjive

print(c)
#ako ovo treba da se vrti cesce lakse je skupiti u cijelinu tj treba napraviti funkciju
#pocetak funkcije je def
def ispis(): #poslije imena funkcije ide zagrada
    print("Ovo je za pocetak.")
    print("Ovo je za pocetak.")
#funkcija mora da se pozove!; pozive je odvojen od funkcije
ispis() # mora da se pozove sa zagradama i onda se ispisuje funkcija!
#podprogram koji sabira 2 broja
def zbir():
    a : int = 3
    b : int = 4 
    c : int = a + b
    print(c)
zbir()
'''funkcija obicno ne bi trebala da ispisuje i racuna; znaci ili jedno ili drugo samo
funkcijama ne bi trebalo davati ista imena i trebala bi u opisu da kaze sta radi'''
zbir()
zbir()
zbir()
zbir()
zbir()
zbir()
'''ustedjuje se pisanje koda, posto radi stalno isto, moze da se stavi isto u for petlju!
funkcije su lose kad su hard kodovane sa fuksim vrijednostima.
u primjeru isopd nisu fiksirani argumenti, pri ispisu se daju argumenti!'''

def zbir2(a,b): #a,b su argumenti!!!
    c : int = a + b
    print(c)
zbir2(10,15)
d = zbir2(10,15)
print(d) #None; zato sto nema vrijednosti posto funkcija nista ne vraca!

#vracanje vrijednosti funkcije!

def zbir3(a,b): 
    c : int = a + b
    return c #vraca vrijednost!
zbir3(10,15)
d = zbir3(10,12) # d postaje zbir3 zato sto smo napisali return c
print(d) #preko d se sacuva rezultati u promjenjivu!!!
print(zbir3(10,12)) #samo ispisuje vrijednost
#funkcije koje racunaju obicno imaju return; funkcije za ispis obicno nemaju
#ima vise nacina za return; ovo je klasican nacin!


def zbir4(a: int, b: int) -> int: #sa stelicom se definse koji je tip povratna vrijednost!
    c : int = a + b
    return c

def zbir5(a: int, b: int) -> int: #c nije potrebno zato sto se vraca povratna vrijednost!
    return a + b

def zbir6(a: int, b: int = 7) -> int: #b je defaultna vrijdnost; ako se nista ne unese stavice 7
    return a + b
print(zbir6(3,5)) #racuna 3+5
print(zbir6(3))   #racuna 3+7


def zbir7(a: int = 9, b: int = 7) -> int: #a i b su defaultna vrijdnost; ako se nista ne unese stavice 7
    return a + b
print(zbir7(3,5)) #racuna 3+5
print(zbir7())   #racuna 9+7


def zbir8(*a) -> int: #5 6 6 5 89 vraca sve sto se unese
    for i in a:
        print(i, end=" ")
zbir8(5,6,6,5,89)
print("-----------")

#da vrati najvice od 3 unesena

def max_od_3(a: float, b: float, c: float) -> float:
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
print(max_od_3(7,5,12))

#funkcija suma prvih n brojeva

def suma(n: int) -> int:
    s = 0
    for i in range(1,n+1):
        s += i
    return s
print(suma(100))

def fun1():
    print("Ja sam prva funkcija")
def fun2():
    print("Ja sam druga funkcija")
    fun1()
fun2() # Ja sam prva funkcija; zato sto se poziva fun1;
def fun3():
    print("Ja sam treca funkcija")
    fun2()
    fun1()
fun3() #2 puta je napisano da je prva funkcija, zato sto se u drugoj vec nalazi prva!!!
'''
def f(): #funkcija poziva samu sebe
    print("nema kraj")
    f()
#f() #ova funkcija nema kraja, posto sve vrijeme smau sebe poziva!!!
#RecursionError: maximum recursion depth exceeded'''
def f(n): 
    if n==0:
        return #return prekida funkciju kad nema nista iza
    print("nema kraj", n)
    f(n-1)
f(5)
