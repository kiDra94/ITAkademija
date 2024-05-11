#objektno programiranje cas 2
#imenski prostor
name = 'global'

def a():
    def b():
        print(name)
    b()

a()

name = 'global'

def a():
    name = 'enclosing'
    def b():
        print(name)
    b()

a()

name = 'global'

def a():
    name = 'enclosing'
    def b():
        name = 'local'
        print(name)
    b()

a()

def outer_function(msg):
    message = msg
 
    def inner_function():
        print(message)
        return 1
 
    return inner_function  # vezivanje povratne vrednosti za funkciju inner_function
 
my_function = outer_function('Hi!')
print(type(my_function))
my_function()
print(type(my_function()))

def kvadrat():
    print("Kvadrat")
 
def my_decorator(function_to_decorate):
    def wrapper_around_original_function():
        print("I am a code running before the original function.")
 
        function_to_decorate()
 
        print("And I am the code that runs after")
 
    return wrapper_around_original_function
 
kvadrat()
my_decorator(kvadrat)()

print("------------------")
 
 
@my_decorator
def kub():
    print("Kub")
 
kub()

def milk(func):
    def wrapper():
        print("hot milk")
        func()
    return wrapper
 
def sugar(func):
    def wrapper():
        print("sugar")
        func()
    return wrapper
 
 
@sugar
@milk
def coffee(variety="arabica"):
    print(variety)
 
'''coffee = sugar(milk(coffee)) 
coffee()
sugar(milk(coffee)())'''
 
 
coffee()
#milk(coffee)()
#sugar(milk(coffee))()
 
'''nesto = milk(coffee)
nesto()'''

#eksperimentisanje!
#----------------------------------
x = 9
def fun(c):
    b = 3
    x = 7
    print(x)
    def fun2():
        pass
    locals()['b'] = 90
    print(locals())
    print("OVO ",locals()['b'])
fun(0)
print(x)
print("----------------------")
globals()['x'] = 19
print(globals())

'''x = 9
def fun3():
    x += 7 # vidi x kao lokalnu promjenjivu; i zato ne moze da prepozna globalni x pa izbacuje error
    print(x)
fun3() '''

x = 9
def fun3(x):
    x += 7
    print(x)
    print(locals())
fun3(5)
 
 
x = 9
def uvecaj(x):
    x+=1
    return x
 
x = uvecaj(x)
print(x)
