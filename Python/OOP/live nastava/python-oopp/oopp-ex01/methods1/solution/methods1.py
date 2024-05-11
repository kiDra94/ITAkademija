class Car: 
    make = ""
    model = ""
    numDoors = 0 
    wheels = 4
    def printDetails(self):
        print("Make: " + self.make)
        print("Model: " + self.model)
        print(f"Number of doors: {self.numDoors}")
        print(f"Number of wheels: {self.wheels}") 

car = Car() 
car.make = "Wolkswagen"
car.model = "Beetle"
car.numDoors = 4;
car.printDetails()
