class Reservoir:
    def __init__(self):
        self.reserveLimit = 10
        self.totalAmount = 100

    def reserveIndicator(self):
        print("Warning, low fuel level!")

    def getFuel(self):
        self.totalAmount -=1
        
        if self.totalAmount <=self.reserveLimit:
            self.reserveIndicator()
        print(self.totalAmount)

res = Reservoir()


for i in range(100):
    res.getFuel()
