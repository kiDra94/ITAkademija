import random as rd

# funkcija koja generiše slučajan realni broj u intervalu (a,b)
def raspon(a:int, b:int) -> float:
    if a >= b:
        return None
    return (b-a)*rd.random() + a

print(raspon(3,7))
print(raspon(7,3))


# funkcija koja kreira listu od n slučajnih brojeva iz intervala (a,b)
def pravi_listu_slucajnih_brojeva(a, b, n):
    X = []
    for _ in range(n):
        X.append((b-a)*rd.random()+a)
    return X

def pravi_listu_slucajnih_brojeva2(a, b, n):
    return [(b-a)*rd.random()+a for _ in range(n)]

def pravi_listu_slucajnih_brojeva3(a, b, n):
    return [raspon(a, b) for _ in range(n)]

a = 3
b = 7
n = 1000
print(pravi_listu_slucajnih_brojeva(a, b, n))
print(pravi_listu_slucajnih_brojeva2(a, b, n))
print(pravi_listu_slucajnih_brojeva3(a, b ,n))