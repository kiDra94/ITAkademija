from abc import ABC, abstractmethod
#class Bird(ABC):
class Bird():
    def __init__(self, name):
        self.name = name

    #@abstractmethod
    def fly(self):
        raise AttributeError(self.name + ' object has no attribute fly')
        #raise NotImplementedError("You have to implement fly() method")

    def walk(self):
        print(self.name + " bird can walk")

class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print("It eats mostly " + str(self.ration))

    def swim(self):
        print(self.name + " bird can swim")

class FlyingBird(Bird):
    def __init__(self, name, ration=None):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print("It eats mostly grains")

    def fly(self):
        print(self.name+" bird can fly")

    def __str__(self):
        return self.name + " bird can walk and fly"

class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return self.name + " bird can walk, swim and fly"

b = Bird("Any")
b.walk()
#"Any bird can walk"

p = NonFlyingBird("Penguin", "fish")
p.swim()
#"Penguin bird can swim"
#p.fly()
#AttributeError: 'Penguin' object has no attribute 'fly'
p.eat()
#"It eats mostly fish"

c = FlyingBird("Canary")
print(c)
#"Canary bird can walk and fly"
c.eat()
#"It eats mostly grains"

s = SuperBird("Gull")
print(s)
#"Gull bird can walk, swim and fly"
s.eat()
#"It eats mostly fish"
print(SuperBird.__mro__)