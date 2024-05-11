class Car: 
    make = ""
    model = ""
    numDoors = 0 
    wheels = 4
    def printDetails(self):
        print("Make: " + self.make)
        print("Model: " + self.model)
        print("Number of doors: " + self.numDoors) 

car = Car()
car.printDetails()

