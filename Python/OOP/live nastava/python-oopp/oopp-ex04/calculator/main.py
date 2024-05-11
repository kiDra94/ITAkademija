class Calculator:
    @staticmethod
    def calculate(a, b, op):
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "/":
            return a / b
        if op == "*":
            return a * b 
        return 0
     
x = Calculator.calculate(5,0,"/")
print(x)


