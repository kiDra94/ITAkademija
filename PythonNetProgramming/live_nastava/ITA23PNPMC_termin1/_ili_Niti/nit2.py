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
t1.start() #pokrece nit iznad
time.sleep(1) #pokrece glavu nit (koja spava n sekundi), radi nit iznad
stop_threads = True #kad nakon n sekundi glavna nit proradi, stop postaje true i nit staje!
t1.join() #poruka glavnoj niti da saceka da zavrsi sporedna nit, pa tek onda glavna da zavrsi!
print('thread killed')
#isto s alambda
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