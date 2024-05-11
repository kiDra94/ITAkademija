#kopija sa casa setova rijecnika i torki
a = (1,1,2)
print(type(a))
for i in a:
    print(i)
for i in range(len(a)):
    print(a[i],end=" ")
print() 
#a[1]=9
print(a.count(1))
a = 2,3
print(type(a))
a =(1,)
print(type(a))
(c,d) = (5,7)
print(c)
 
a = {4,5,5,5}
print(a)
a.add(7)
print(a)
a.add(7)
print(a)
#print(a[2])
a = set()
print(type(a))
a.add(9)
print(a)
print(type({5}))
c = {}
print(type(c))
d = {"god":37,"ime":"Pera","br stanje":1,"a":{"por":["Mama","Tata"]}}
print(type(d))
print(d["god"])
d["info"]=7
print(d)
d["god"]=39
print(d)
print(d["a"]["por"][0])
d[2]="Nesto"
print(d)
 