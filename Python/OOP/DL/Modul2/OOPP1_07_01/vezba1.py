class Card:
    def __init__(self,number,balance):
        self.number = number
        self.balance = balance

    def pay(self,amount):
        self.balance = self.balance - amount


class Visa(Card):
    tax = 5/100
    def pay(self,amount):
        super().pay(amount)
        self.balance = self.balance - amount * self.tax

class Master(Card):
    tax = 8/100
    def pay(self,amount):
        super().pay(amount)
        self.balance = self.balance -  amount * self.tax

    
c = Visa("123",954)
c.pay(75)
print(c.balance)
c = Master("234",954)
c.pay(75)
print(c.balance)