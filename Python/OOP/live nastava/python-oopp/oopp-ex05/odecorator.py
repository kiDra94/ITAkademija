class decorator:
    def __init__(self,op):
        self.op = op

    def __call__(self,f): 
        if self.op == "+":  
            return lambda a,b : a + b
        elif self.op == "-":
            return lambda a,b : a - b

@decorator("-")
def f1(a,b): 
    pass
@decorator("+")
def f2(a,b): 
    pass
  
print(f1(4,3))
print(f2(4,3))


