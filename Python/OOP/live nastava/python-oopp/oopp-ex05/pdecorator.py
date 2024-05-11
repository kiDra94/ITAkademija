def decorator(oper):  
    def inner(f): 
        if oper == "+":
            return lambda a,b : a + b
        elif oper == "-":
            return lambda a,b : a - b   
        return f
    return inner 

@decorator("-")
def f1(a,b): 
    pass
@decorator("+")
def f2(a,b): 
    pass
  
print(f1(4,3))
print(f2(4,3))