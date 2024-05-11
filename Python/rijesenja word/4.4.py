def addition(*arguments):
    s = 0
    for i in arguments:
        s += i
    return s

suma=addition(2,1,3,4)
print("Addition:",suma)
