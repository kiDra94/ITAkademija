#ispisi rucnu na papiru sta se desava
#cormen algoritmika
n =  3
a =[0]*n
def fun(n,a,i):
    if(i==n):
        print(a)
        return
    a[i] = 0
    fun(n,a,i+1)
    a[i] = 1
    fun(n,a,i+1)
fun(n,a,0)
print("-----------------")
#praktican primjer tezina i kapacitet
import random
n =  10
a =[0]*n
t = [] 
kap = 40
max = 0
for i in range(n):
    t.append(kap*random.random()) # random.random vraca brojev izmedju 0 i 1, tako da stavka t ne moze da predje kapacitet
print(t)
def fun(n,a,i,tezina):
    global max #nije optimalno rijesenje zbog global!!!
    if(i==n):
        if tezina > max and tezina <= kap:
            max = tezina
            print(a) #posljednja stavka je maksimum
        return
    a[i] = 0
    fun(n,a,i+1,tezina+a[i]*t[i])
    a[i] = 1
    fun(n,a,i+1,tezina+a[i]*t[i])
fun(n,a,0,0)
print("Max popunjenost: ", max)
'''#praktican primjer tezina i kapacitet
n =  3 # ovo ne radi kako treba cisto da znas XD
a =[0]*n
t = [6, 12, 15]
kap = 20
max = 0
def fun(n,a,i,tezina,maxi):
    if(i==n):
        print(maxi)
        return
    a[i] = 0
    if tezina+a[i]*t[i] > maxi and tezina+a[i]*t[i] < kap:
        maxi = tezina+a[i]*t[i]
    fun(n,a,i+1,tezina+a[i]*t[i],maxi)
    a[i] = 1
    fun(n,a,i+1,tezina+a[i]*t[i],maxi)
fun(n,a,0,0,0)'''
