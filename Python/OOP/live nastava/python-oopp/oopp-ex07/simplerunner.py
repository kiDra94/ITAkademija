import _thread, time

def handler(i):  
    id = _thread.get_ident()
    print(f"Hello from thread: {i}")
    print(f"Thread id: {i}")

for i in range(10):
    id = _thread.start_new_thread(handler,(i,))
    print(f"Created thread with id: {id}")

time.sleep(1)


