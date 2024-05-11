#isti cas kao opp5 i opp6
class Osnovna:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self._d = 100 # _d == protekted; ne radi kako treba, mogu mu sva djeca i djeca od djecije djece pristupiti
        # __d -> private; djete moze samo preko metode klasse da pristupi; tagovano kod izvedene!
    def pristupi(self):
        print(self._d)

    def __str__(self):
        return str(self.a)+" "+str(self.b)

class Izvedena(Osnovna):
    def __init__(self,a,b,c):
        super().__init__(a,b) # self.a = a, self.b = b
        self.c = c
        print("Izvedena ",self.a,self.b,self.c)

    def pristupi(self):
        # super().pristupi()
        print(self._d)

    def __str__(self):
        return super().__str__()+" "+str(self.c)

o = Osnovna(7,3)
i = Izvedena(9,1,5)
print(o)
print(i)
o.pristupi()
i.pristupi()

