try:
    x=100/0
except:
    print("Hey, you can't divide by zero!")
'''try:
    x=100/0
    y=10
except:
    print("Hey, you can't divide by zero!")
 
print(y)'''

try:
    x=100/0
except ZeroDivisionError:
    print("Hey, you can't divide by zero!")

try:
    x=100/0
except NameError:
    print("You won't see me!")
except ZeroDivisionError:
    print("Hey, you can't divide by zero!")
except Exception:
    print("I'm here just in case you didn't find anything")

try:
    x=100
    y=0
    print(x/y)
except NameError:
    print("You won't see me!")
except ZeroDivisionError:
    print("Hey, you can't divide by zero!")
except Exception:
    print("I'm here just in case you didn't find anything")
finally:
    print("Value of y is: ",y)

def divide(a,b):
    if b == 0:
        return 0
 
    if a>10 or b>10:
        raise ArithmeticError("Number is larger than 10")
 
    else:
        return a/b
 
print(divide(14,2))

