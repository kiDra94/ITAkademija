import reservoir
import time

res = reservoir.Reservoir() 

class MyListener(reservoir.EventListener):
    def reserve_reached(self, sender):
        print("No more fuel in car. Please refill!")

res.add_listener(MyListener())

for i in range(0,100):
    res.consume_fuel()
    time.sleep(0.1);


