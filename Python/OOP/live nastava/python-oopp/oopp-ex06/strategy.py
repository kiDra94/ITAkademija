class Bankomat: 
    def __init__(self,balance):
        self.balance = balance
    def doPayment(self,strategy,amount):
        self.balance -= strategy.calculate(amount)

class VisaStrategy:
    def calculate(self,amount):
        return amount * 1.2

class MasterStrategy:
    def calculate(self,amount):
        return amount * 1.4
    
b = Bankomat(100)
b.doPayment(VisaStrategy(),10)
print(b.balance)
b = Bankomat(100)
b.doPayment(MasterStrategy(),10)
print(b.balance)

