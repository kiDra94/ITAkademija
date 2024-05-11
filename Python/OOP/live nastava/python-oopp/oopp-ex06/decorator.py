class Card:
    balance = 100
    def pay(self,amount):
        self.balance = self.balance - amount

class Visa:
    def __init__(self,card):
        self.card = card
    def pay(self,amount):
        self.card.pay(amount * 1.2)

v = Visa(Card())
v.pay(10) 
print(v.card.balance)  

