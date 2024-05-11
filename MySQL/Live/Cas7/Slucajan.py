import random as rd
print(rd.randint(3, 7)) #random broj izmedju 3 i 7
print(round(rd.random(),2)) # broj izme. 0 i 1
print(round(7*rd.random(),3)) # ,3 znaci 3 iza kome
#a = int(input("Unesi broj: "))
#print(round(a*rd.random(),3))
# generisati od b-a + a
def fun(a, b):
    return round((b-a)*rd.random()+a, 2)

print(fun(3, 7))

'''#info _ u petlji se stavlja kad "i" ne utice na petlju; tako da _ zauzima mjesto
for _ in range(1000):
    print("*", end="")'''

def raspon(a, b, c):
    lista = []
    for _ in range(c):
        lista.append(round((b-a)*rd.random()+a, 2))
    return lista
print(raspon(3, 7, 8))

#listcomprehension
def raspon1(a, b , c):
    return [(round((b-a)*rd.random()+a, 2)) for _ in range(c)]
print(raspon1(3, 7, 8))

def sluc(a, b):
    return round((b-a)*rd.random()+a, 2)

def raspon2(a, b , c):
    return [sluc(a, b) for _ in range(c)]
print(raspon2(3, 7, 8))

class Raspon:
    def raspon2(self, a, b , c):
        return [sluc(a, b) for _ in range(c)] 
obj = Raspon()
print(obj.raspon2(3, 7, 8))