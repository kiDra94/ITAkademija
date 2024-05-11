def calc(a,b,op):
    if op == "add":
        return a + b
    elif op == "sub":
        return a - b
    elif op == "mul":
        return a * b
    elif op == "div":
        return a / b
    else:
        return 0 

print(calc(2,5.545,"mul"))