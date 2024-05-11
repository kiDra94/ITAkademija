import threading, time, random

class Snail(threading.Thread):
    def __init__(self,id):
        super().__init__()
        self.id = id

    def run(self):
        total_trip = 10
        while total_trip > 0:
            total_trip -= 1
            time.sleep(random.randint(1,5))   
            print(f"{total_trip}".rjust(self.id))
        print(f"Snail #{self.id} finished")


for i in range(50):
    Snail(i).start()

