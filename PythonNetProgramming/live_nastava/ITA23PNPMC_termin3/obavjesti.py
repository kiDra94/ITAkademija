import time
from threading import *
import random


class appointment:

    def patient(self):
        condition_object.acquire() #sluzi kao katanac; da druga nit ne moze da se petlja
        print('patient john waiting for appointment')
        condition_object.wait()  # Thread is in waiting state; ceka dok ne stigne obavjestenje!!!
        print('successfully got the appointment')
        condition_object.release() #otkljucava kad zavrsi 

    def doctor(self):
        condition_object.acquire()
        print('doctor jarry checking the time for appointment')
        time = random.randint(1, 13)
        print('time checked')
        print('appointed time is {} PM'.format(time))
        condition_object.notify() #salje obavjestenje; kako bi patient nastavio dalje da radi
        condition_object.release()


condition_object = Condition() #ugradjenja klasa; to je u sustini brava
class_obj = appointment()

T1 = Thread(target=class_obj.patient)
T2 = Thread(target=class_obj.doctor)

T1.start()
T2.start()

T1.join()
T2.join()