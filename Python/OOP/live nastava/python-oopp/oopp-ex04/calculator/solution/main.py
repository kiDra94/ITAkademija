class CalculatorNotNumberException(Exception): pass
class CalculatorZeroDivisorException(Exception): pass
class CalculatorInvalidOperationException(Exception): pass

class Calculator:
    @staticmethod
    def calculate(a, b, op):
        if not isinstance(a, int) or not isinstance(b,int):
            raise CalculatorNotNumberException()
        if b == 0:
            raise CalculatorZeroDivisorException()
        if not op in ["+","-","*","/"]:
            raise CalculatorInvalidOperationException()
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "/":
            return a / b
        if op == "*":
            return a * b 
        return 0
    
try:
    x = Calculator.calculate(5,2,"=")
    print(x)
except CalculatorNotNumberException:
    print("Operand is not a number")
except CalculatorInvalidOperationException:
    print("Operator is not valid")
except CalculatorZeroDivisorException:
    print("You cannot divide with zero")
except Exception:
    print("Only God knows what is the problem")