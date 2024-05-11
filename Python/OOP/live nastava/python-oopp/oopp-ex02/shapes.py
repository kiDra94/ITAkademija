class Shape: 
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = "" 

class Rectangle(Shape): 
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a*self.b

class Square(Shape):
    def __init__(self,a):
        self.a = a
    def area(self):
        return self.a**2

class Circle(Shape):
    PI = 3.14;
    def __init__(self,r):
        self.r = r
    def area(self):
       return self.r * self.r * Circle.PI;  


c = Circle(2)
print("Circle area: " , c.area())
r = Rectangle(2,3)
print("Rectangle area: " , r.area())
s = Square(3)
print("Square area: " , s.area())