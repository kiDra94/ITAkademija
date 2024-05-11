from threading import Thread, Lock
from time import sleep
#ako se sklone lock ne radi kako treba! vidi fajl ks
counter = 0

def increase(by, lock):
    global counter

    lock.acquire() #zakljuca kriticnu sekciju, tj t1 odradi sve do kraja, tek onda t2 krece

    local_counter = counter
    local_counter += by

    sleep(0.1)

    counter = local_counter
    print(f'counter={counter}')

    lock.release()


lock = Lock()

# create threads
t1 = Thread(target=increase, args=(10, lock))
t2 = Thread(target=increase, args=(20, lock))

# start the threads
t1.start()
t2.start()


# wait for the threads to complete
t1.join()
t2.join()


print(f'The final counter is {counter}')