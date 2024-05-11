#ppf ex 09 calc.py
def calculator(a: int, b: int, msg: str) -> int:
    if msg == "add":
        return a+b
    elif msg == "sub":
        return a-b
    elif msg == "div":
        return a/b
    elif msg == "mul":
        return a*b
    else:
        return "Wrong operation"
print(calculator(5.44,6,"add"))