class Calculator:
    operand1 = 0.0
    operand2 = 0.0
    def add(self):
        return self.operand1 + self.operand2
    def sub(self):
        return self.operand1 - self.operand2
    def mul(self):
        return self.operand1 * self.operand2
    def div(self):
        return self.operand1 / self.operand2

calc = Calculator()
calc.operand1 = 3
calc.operand2 = 2
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())