import abc
class EventListener(abc.ABC):
    @abc.abstractmethod
    def reserve_reached(self,sender):
        pass 

class Reservoir:
    def __init__(self):
        self.current_state = 100
        self.reserve_limit = 50
        self.listeners = []  

    def add_listener(self, listener):
        self.listeners.append(listener)

    def remove_listener(self, listener):  
        self.listeners.remove(listener)

    def distribute_event(self):
        for listener in self.listeners:
            if isinstance(listener, EventListener):
                listener.reserve_reached(self)
    
    def consume_fuel(self):
        print(f"Fuel consumed. {self.current_state} liters remaining")
        self.current_state -= 1
        if self.current_state < self.reserve_limit:
            self.distribute_event() 


            