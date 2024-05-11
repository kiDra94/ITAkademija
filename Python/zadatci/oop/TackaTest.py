import Tacka as t

t3 = t.Tacka()
print(type(t3))
a = 7
print(type(a))
print(isinstance(a,int))
#print(t3.__dict__)
print(t3)
t4 = t.Tacka(1,2) # t4.x = 1, t4.y = 2 stari komentari
t5 = t.Tacka(1,2) # t5.x = 2, t5.y = 3
print(t4.rastojanje(t5)) # self = t4, t = t5
print(t4.jednake(t5))
print(id(t4))
print(id(t5))
print(t4==t5)
a = 8
b = 7
print(b==a)
print(a+b)
print(t4+t5)
t6 = t4+t5
print(t6)