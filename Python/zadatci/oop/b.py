#import a
 
#a.f1()
 #odavde
from a import f1 as f
from a import f2
 
#from a import *
 
 
print("Pozvano iz B ",__name__)
 
#f1()
f()
f2()
#dovde komentar ako hoces c da radi
def foo():
    print("BBB")
 
def func1(): 
    from a import func2 
    pass
 