class Card:
    def __init__(self,number,balance):
        self.number = number
        self.balance = balance
    def pay(self,amount):
        self.balance = self.balance - amount

class Visa(Card):
    tax = 0.5
    def pay(self,amount):
        super().pay(amount)
        self.balance = self.balance - (amount * self.tax) 

class Master(Card):
    tax = 0.8
    def pay(self,amount):
        super().pay(amount)
        self.balance = self.balance - (amount * self.tax) 
    
c = Visa("123",100)
c.pay(10)
print(c.balance)
c = Master("234",100)
c.pay(10)
print(c.balance)