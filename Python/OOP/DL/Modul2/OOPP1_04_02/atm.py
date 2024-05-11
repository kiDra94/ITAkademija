class Card:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
class Atm:
    def __init__(self):
        self.card = None
    def set_card(self,card):
        self.card = card
    def withdraw(self,amount):
        if self.card:
            if self.card.balance - amount >= 0:
                self.card.balance -= amount
                print(f"Success, new balance: {self.card.balance}")
            else:
                print("Error, not enough funds")
        else:
            print("Card not set")

bank = Atm()
card = Card("Visa",100)
bank.set_card(card)
bank.withdraw(8) 