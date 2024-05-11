def divide(a,b):
        if b==0:
            return 0
        if a>10 or b>10:
            raise ArithmeticError("Larger than 10")
        else:
            return a+b 
try:
    print(divide(14,1))
except ArithmeticError as ex: 
    print(ex) 

    