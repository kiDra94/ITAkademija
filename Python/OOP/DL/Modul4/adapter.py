class EuropeanSocket:
    def voltage(self): pass
     
class Socket(EuropeanSocket):
    def voltage(self):
        return 230
    
class USASocket:
    def voltage(self): pass

class Adapter(USASocket):
    __socket = None
 
    def __init__(self, socket):
        self.__socket = socket
 
    def voltage(self):
        return 110
    
class ElectricKettle:
    __power = None
 
    def __init__(self, power):
        self.__power = power
 
    def boil(self):
        if self.__power.voltage() > 110:
            print ("Kettle on fire!")
        else:
                print ("Coffee time!")

socket  = Socket()
adapter = Adapter(socket)
kettle  = ElectricKettle(adapter)
 
kettle.boil()