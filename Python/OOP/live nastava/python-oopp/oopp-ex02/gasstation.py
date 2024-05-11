import abc 
class BaseStation(abc.ABC):
    @abc.abstractmethod
    def fillCar(self): pass

class ShellGasStation(BaseStation):
    def fillCar(self):
        print("Filling car with water")

shell = ShellGasStation()