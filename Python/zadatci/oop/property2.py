class Car:
    def __init__(self):
        self.fuel_amount = 0

    @property #ugradjen dekorator!
    def fuel_amount(self):
        print("EVO")
        return self._fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, amount):
        if amount < 0:
            raise ValueError("Tank can't be less than empty!")

        if amount > 60:
            raise ValueError("Tank can't take more than 60 l!")

        self._fuel_amount = amount
        
car = Car()
car.fuel_amount = 50
print(car.fuel_amount)
#car.fuel_amount = 70 #izbacuje error! zbog if petlje
#print(car.fuel_amount)