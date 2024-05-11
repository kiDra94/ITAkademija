import math
import typing
class Tacka:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
 
    def rastojanje(self,t):
        return math.sqrt((t.x-self.x)**2+(t.y-self.y)**2)
 
    def __str__(self):
        return f"Tacka igleda: ({self.x},{self.y})"
 
    def kopiraj(self,t):
        self.x = t.x
        self.y = t.y
 
    def jednake(self,t):
        '''if self.x == t.x and self.y == t.y:
            return True
        return False'''
        if isinstance(t, Tacka):
            return self.x == t.x and self.y == t.y
        return False
 
    def __eq__(self, t):
        print("Poziva se equal")
        if isinstance(t, Tacka):
            return self.x == t.x and self.y == t.y
        return False
 
    def __add__(self, t):
        return Tacka(self.x + t.x, self.y + t.y)
 
if __name__=="__main__":
    t1 = Tacka()
    print(t1.__dict__)
    t2 = Tacka(3,4)
    print(t2.__dict__)
    print(t2)
    t1.kopiraj(t2)
    print(t1)
    t1.x = 7
    print(t1)
    print(t2)
    print("---------")
    t1 = t2
    print(t1)
    print(t2)
    t1.x = 7
    print(t1)
    print(t2)
    print(Tacka.__dict__)