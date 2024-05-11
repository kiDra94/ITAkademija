class SixtyLitresCapacity:    
    def __set__(self, owner : object, amount):
        if amount < 0:
            raise ValueError("Tank can't be less than empty!")

        if amount > 60:
            raise ValueError("Tank can't take more than 60 l!")

        owner._fuel_amount = amount

    def __get__(self, owner : object, objtype=None):
        return owner._fuel_amount

class Car2:

    fuel_amount = SixtyLitresCapacity()

    def __init__(self):
        self.fuel_amount = 0
        
        
car = Car2()
car.fuel_amount = 50
print(car.fuel_amount)
#car.fuel_amount = 70
#print(car.fuel_amount)