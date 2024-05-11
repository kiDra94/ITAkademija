#isti cas kao opp5 i opp6
import math
from abc import ABC, abstractmethod

class GeoSlika(ABC):
    @abstractmethod
    def povrsina(self):
        pass

class Krug(GeoSlika):
    def __init__(self,r):
        self.r = r

    def povrsina(self):
        return self.r**2*math.pi

class Pravougaonik(GeoSlika):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def povrsina(self):
        return self.a*self.b
    
k = Krug(7)
p = Pravougaonik(2,3)
#print(k.povrsina())
#print(p.povrsina())
niz = [Krug(i) if i%2==0 else Pravougaonik(i,i+1) for i in range(1,16)]
#for x in niz:
    #print(x.povrsina())
for x in niz:
    if isinstance(x,Krug) and x.povrsina() > 200:  
        print(x.povrsina())


#g = GeoSlika()