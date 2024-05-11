#print("A")
#print("Trava raste")
 
def f1():
    print("Ovo je f1 iz A")
 
def foo():
    print("AAA")
 
def func2(): 
    from b import func1 
    pass
 
#print("Pozvano iz A ",__name__)
 
if __name__=="__main__":
    print("Trava raste")