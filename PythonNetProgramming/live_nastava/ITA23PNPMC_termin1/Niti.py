----------------------SINGLETON DESIGN PATTERN------------------------------------------------------

A singleton is a class that only allows a single instance of itself to be created and gives access to that created instance. 
Implement singleton logic inside your custom class using a method to initialize a class instance.

Example:

>>> p = Sun.inst()
>>> f = Sun.inst()
>>> p is f
True

class Sun:
    instance = None

    def __init__(self):
        pass

    @classmethod
    def inst(cls):
        if cls.instance is None:
            cls.instance = Sun()
        return cls.instance


p = Sun.inst()
print(id(p))
f = Sun.inst()
print(id(f))
print(p is f)

---

class Sun:
    instance = None

    def __init__(self, cls):
        """ Virtually private constructor. """
        if cls.instance is not None:
            raise Exception("This class is a singleton!")
        cls.instance = self

    @classmethod
    def inst(cls):
        if cls.instance is None:
            cls.instance = Sun()
        return cls.instance


a = Sun(Sun)
print(id(a))
#b = Sun(Sun)
#print(id(b))
p = Sun.inst()
print(id(p))
f = Sun.inst()
print(id(f))
print(p is f)

---

class Sun:
    _instance = None

    def __init__(self):
        """ Virtually private constructor. """
        raise Exception("This class is a singleton!")

    @classmethod
    def inst(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance


#a = Sun(Sun)
#print(id(a))
p = Sun.inst()
print(id(p))
f = Sun.inst()
print(id(f))
print(p is f)

---

class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        Singleton.__instance = self  # Ovo sada omogućava kreiranje različitih objekata


s = Singleton()
print(id(s))

s = Singleton()
print(id(s))

s = Singleton.getInstance()
print(id(s))

s = Singleton.getInstance()
print(id(s))

---

class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


s = Singleton()
print(id(s))

s = Singleton()
print(id(s))

s = Singleton.getInstance()
print(id(s))

s = Singleton.getInstance()
print(id(s))

----------------------OBSERVER DESIGN PATTERN------------------------------------------------------

from ConcreteObserver import Shop  
from ConcreteSubject import Pen  
      
pen = Pen(10)  
pen.add(Shop('Shop1'))  
pen.add(Shop('Shop2'))  
pen.add(Shop('Shop3'))  
  
pen.penPrize = 15  
pen.penPrize = 20  
pen.penPrize = 32  

subject.py:

from abc import ABC, abstractmethod  
      
class PenSubject(ABC):  
     
    @abstractmethod  
    def add(self, shop):  
            pass  
        
    @abstractmethod  
    def remove(self, shop):  
            pass  
        
    @abstractmethod  
    def notify(self):  
            pass  
            
observer.py:

from abc import ABC, abstractmethod  
      
      
class ShopObserver(ABC):  
     
    @abstractmethod  
    def update(self, pen):  
        pass  


ConcreteSubject:

from subject import PenSubject  
      
      
class Pen(PenSubject):  
      
    def __init__(self, prize):  
        self._penPrize = prize  
  
    shops = []  
  
    def add(self, shop):  
        self.shops.append(shop)  
  
    def remove(self, shop):  
        self.shops.remove(shop)  
  
    def notify(self):  
        for shop in self.shops:  
            shop.update(self)  
        print('---------------------------------------')  
 
    @property  
    def penPrize(self):  
        return self._penPrize  
 
    @penPrize.setter  
    def penPrize(self, prize):  
        self._penPrize = prize  
        self.notify() 

ConcreteObserver:


from observer import ShopObserver  
from ConcreteSubject import Pen  
      
      
class Shop(ShopObserver):  
      
        def __init__(self, shopName: str):  
            self._shopName = shopName  
      
        def update(self, pen: Pen):  
            print("pen prize changed to ", pen.penPrize, ' in ', self._shopName)
            

------------------THREADS---------------------------- 

import threading #potreban da se pravi Nit

def worker():
    """thread worker function"""
    print('Worker')
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker) #Thrad je ugradnjea klasa -> mora da se navede sta ce Nit raditi; ovdje pise target=worker(to je metoda!)
    threads.append(t)
    t.start()
    
for i in range(5):
    print(id(threads[i]))
    
---

import threading

def worker(num):
    """thread worker function"""
    print('Worker: %s' % num)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

---

import threading
import time

def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')

def my_service():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(), 'Exiting')

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker) # use default name

w.start()
w2.start()
t.start()

---


# Python program showing
# how to kill threads
# using set/reset stop
# flag
 
import threading
import time
 
def run():
    while True:
        print('thread running')
        global stop_threads
        if stop_threads:
            break
 
stop_threads = False
t1 = threading.Thread(target = run)
t1.start()
time.sleep(1)
stop_threads = True
t1.join()
print('thread killed')


---

# Python program killing
# threads using stop
# flag
 
import threading
import time
 
def run(stop):
    while True:
        print('thread running')
        if stop():
                break
                 
def main():
        stop_threads = False
        t1 = threading.Thread(target = run, args =(lambda : stop_threads, ))
        t1.start()
        time.sleep(1)
        stop_threads = True
        t1.join()
        print('thread killed')
main()

stop_threads = True
stop = lambda : stop_threads # funkcija koja uvek vraca vrednost stop_threads
print(type(stop))
print(stop())

---

# Python program creating
# three threads
 
import threading
import time
 
# counts from 1 to 9
def func(number):
    for i in range(1, 10):
        time.sleep(0.01)
        print('Thread ' + str(number) + ': prints ' + str(number*i))
 
# creates 3 threads
for i in range(0, 3):
    thread = threading.Thread(target=func, args=(i,))
    thread.start()
    if i%2==0:
        thread.join()

    
print("------------------------") 


---

import threading
import time
import sys
 
def func():
    while True:
        time.sleep(0.5)
        print("Thread alive, and it won't die on program termination")
 
t1 = threading.Thread(target=func)
t1.start()
time.sleep(2)
sys.exit()
print("----------------------")


'''
The difference between daemon threads and non-daemon threads is that the process 
will exit if only daemon threads are running, whereas it cannot exit 
if at least one non-daemon thread is running.
'''

---

import threading
import time
import sys
 

def func():
    while True:
        time.sleep(0.5)
        print("Thread alive, and it will die on program termination")
 
t1 = threading.Thread(target=func)
t1.daemon = True
#t1.setDaemon(True)
t1.start()
time.sleep(2)
print("----------------------")
sys.exit()



'''
The difference between daemon threads and non-daemon threads is that the process 
will exit if only daemon threads are running, whereas it cannot exit 
if at least one non-daemon thread is running.
'''

---

# example of creating a new daemon thread
from time import sleep
from threading import current_thread
from threading import Thread
 
# function to be executed in a new thread
def task():
    # get the current thread
    thread = current_thread()
    # report if daemon thread
    print(f'Daemon thread: {thread.daemon}')
 
# create a new daemon thread
thread = Thread(target=task, daemon=False)
# start the new thread
thread.start()
# block for a moment to let the daemon thread run
sleep(0.5)

# example of creating a new daemon thread
from time import sleep
from threading import current_thread
from threading import Thread
 
# function to be executed in a new thread
def task():
    # get the current thread
    thread = current_thread()
    # report if daemon thread
    print(f'Daemon thread: {thread.daemon}')
 
# create a new daemon thread
thread = Thread(target=task, daemon=True)
# start the new thread
thread.start()
# block for a moment to let the daemon thread run
sleep(0.5)

# example of configuring a thread to be a daemon thread
from time import sleep
from threading import current_thread
from threading import Thread
 
# function to be executed in a new thread
def task():
    # get the current thread
    thread = current_thread()
    # report if daemon thread
    print(f'Daemon thread: {thread.daemon}')
 
# create a new thread
thread = Thread(target=task)
# configure the thread to be a daemon thread
thread.daemon = True
# start the new thread
thread.start()
# block for a moment to let the daemon thread run
sleep(0.5)

---

import threading
                  
class MyThread(threading.Thread):

    def run(self):
        print('running')
        return

for i in range(5):
    t = MyThread()
    t.start()
    
---

import threading
import time

class MyThread(threading.Thread):
  # overriding constructor
  def __init__(self, i):
    # calling parent class constructor
    threading.Thread.__init__(self)
    self.x = i
    
  # define your own run method
  def run(self):
    print("Value stored is: ", self.x)
    time.sleep(3)
    print("Exiting thread with value: ", self.x)
    

thread1 = MyThread(1)
thread1.start()
thread2 = MyThread(2)
thread2.start()

---

import threading, time

class MyThread(threading.Thread):
    
    active = False
    def stop_thread(self):
        self.active = False
        
    def run(self): 
        self.active = True
        print("I am going to sleep 10 seconds")
        for i in range(10000):
            time.sleep(0.1)
            if not self.active:
                return
            print("Thread is running")

mt = MyThread() 
mt.start()  
time.sleep(2)
print("Hey, wake up!")
mt.stop_thread()

---

import threading, time

class Vehicle(threading.Thread):
    
    def stop_thread(self):
        self.active = False
        
    def __init__(self,type): 
        super().__init__()
        self.type = type
        self.fuel = 10
        self.active = True
        if type == "truck":
            self.consumption = .4
            self.speed = 1.5
        else:
            self.consumption = .2
            self.speed = 1

    def run(self):
        #self.active = True
        while True:
            time.sleep(self.speed)
            if self.fuel<=0:
                print(f"Refilling {self.type} tank...")
                time.sleep(4)
                self.fuel=10
            else:
                print(f"{self.type} is running ({self.fuel:.2f})")
                self.fuel-=self.consumption
            if not self.active:
                return

car     = Vehicle("car")
truck   = Vehicle("truck")

car.start()
truck.start()
time.sleep(60)
car.stop_thread()
truck.stop_thread()

----------------RACE CONDITION----------------------

import random
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
                    
class Counter(object):
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start
    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()

def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

logging.debug('Waiting for worker threads')
main_thread = threading.currentThread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Counter: %d', counter.value)

----------------RACE CONDITION----------------------

import threading  
import time 
  
obj1= threading.Condition() 


def task (): 
  
  print('addition of 1 to 10000000 ') 
  #add= 0
  global add
  for i in range (1, 10000001):
    add = add+1 
  print('the condition object is releases now') 
    
add=0
time.sleep(1)
t1 = threading.Thread(target = task) 
t2 = threading.Thread(target = task) 
t1.start() 
t2.start()
t1.join() 
t2.join()
print(add)

print("---------------------------")

obj1= threading.Condition() 


def task (): 
  
  print('addition of 1 to 10000000 ') 
  #add= 0
  global add
  obj1.acquire()
  for i in range ( 1 , 10000001 ):
    add = add+1 
  obj1.release()
  print('the condition object is releases now') 
    
add=0
time.sleep(1)
t1 = threading.Thread(target = task) 
t2 = threading.Thread(target = task) 
t1.start() 
t2.start()
t1.join() 
t2.join()
print(add)

print("---------------------------")

obj1= threading.Condition() 


def task (): 
  
  print('addition of 1 to 10000000 ') 
  #add= 0
  global add
  for i in range ( 1 , 10000001 ):
    obj1.acquire() 
    add = add+1 
    obj1.release() 
  print('the condition object is releases now') 
    
add=0
time.sleep(1)
t1 = threading.Thread(target = task) 
t2 = threading.Thread(target = task) 
t1.start() 
t2.start()
t1.join() 
t2.join()
print(add)

---------------------SABIRANJE MATRICA PREKO JEDNE I PREKO VIŠE NITI--------------------------

X = [[1,2,3],
    [4,5,6],
    [7,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
        
# iterate through rows
for i in range(len(X)):  
# iterate through columns
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
 
for r in result:
    print(r)
    
---

import threading
import logging

X = [[1,2,3],
    [4,5,6],
    [7,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
    
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class MyThread(threading.Thread):

    def __init__(self,i):
        threading.Thread.__init__(self)
        self.i=i

    def run(self):
        logging.debug('running')
        print("Nit ",self.i)
        for j in range(len(X)):
            result[self.i][j]=X[self.i][j]+Y[self.i][j]

t = []
for i in range(len(X)):
    t.append(MyThread(i))
print(t)
for i in range(len(X)):
    t[i].start()
    t[i].join() # zakomentarisati
    #pass

for r in result:
    print(r)
    
----------------------MNOŽENJE MATRICA PREKO JEDNE I PREKO VIŠE NITI-----------------------------------
 
# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix   
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
     
result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
                    
# iterating by row of A
for i in range(len(A)):
 
    # iterating by column by B
    for j in range(len(B[0])):
 
        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
 
for r in result:
    print(r)
    
---

import threading
import logging
 
# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix   
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]
    
result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]


class MyThread(threading.Thread):

    def __init__(self,i,j):
        threading.Thread.__init__(self)
        self.i=i
        self.j=j

    def run(self):
        logging.debug('running')
        print("Nit ",self.i," ",self.j)
        for k in range(len(B)):
            result[self.i][self.j] += A[self.i][k] * B[k][self.j]

t = []
for i in range(len(A)):
    t.append([])
    for j in range(len(B[0])):
         t[i].append(MyThread(i,j))
print(t)
for i in range(len(A)):
    for j in range(len(B[0])):
        t[i][j].start()
        t[i][j].join() # zakomentarisati
        #pass

for r in result:
    print(r)

-------------------------------------------------





















           
        
