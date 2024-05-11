import time
class Distributer:
    __subscribers = []
    def add_subscriber(self,subscriber):
        self.__subscribers.append(subscriber)
    def remove_subscriber(self,subscriber):
        self.__subscribers.remove(subscriber)
    def update(self,evt):
        for sub in self.__subscribers:
            sub.update(evt)

    def do_something(self):
        while True:
            self.update(time.time())
            time.sleep(1) 
        
class Subscriber1:
    def update(self,evt):
        print(f"Subscriber1 received {evt}")

class Subscriber2:
    def update(self,evt):
        print(f"Subscriber2 received {evt}")

d = Distributer()
d.add_subscriber(Subscriber1())
d.add_subscriber(Subscriber2())
d.do_something()

 