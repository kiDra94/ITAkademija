class A:
    x = 10
    y = 15

a = A()
b = A()

print(id(a))
print(id(b))

print(id(a.x))
print(id(b.x))

print(dir(a))

calc = type('X',(),{"a":0,"b":0,"add":lambda self,a,b:a+b})
c = calc()
print(c.add(4,5))
print(type(c))

x = "13"
 
if isinstance(x,int):
    print(x*x)
else:
    print("Not a number")

class Person:
    name ="John"

new_person = Person()
print("Befor name change", new_person.name)

setattr(new_person, "name", "David")

print("After name change", new_person.name)

def x():
  a = 5
 
num1 = 5
num2 = 2
 
z = num1+num2
 
print(callable(x))
print(callable(z))

class Example:
    pass
obj = Example()
 
def new_method(self): # Have to add self since this will become a method
    print('Hello world!')
 
setattr(Example, 'show_text', new_method)
 
obj.show_text()
