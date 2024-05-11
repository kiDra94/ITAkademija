import threading
import time
import sys
 
def func():
    while True:
        time.sleep(0.5)
        print("Thread alive, and it won't die on program termination")
 
t1 = threading.Thread(target=func)
t1.daemon = True #bolja syntaxa
#t1.setDaemon(True)
t1.start()
time.sleep(2)
print("----------------------") #ovo je glavna nit
sys.exit() #zavsava samo glavnu nit
#demonska nit je nit koja se vrti u pozadini; ako se demon zakomentarise se t1 vrti beskonacno
#sa deamon = true progamu se govori da kad stane glavna nit, i pozadinkse zaustavljaju!