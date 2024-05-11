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
    if i%2==0: #0 i 2 nit kaze glavnoj da sacekat; prva moze da "izvisi!"
        thread.join() #pruka glavnoj niti da saceka da se neka druga nit zavrsi; u ovom slucaju su to 0 i 2!

    
print("------------------------") 