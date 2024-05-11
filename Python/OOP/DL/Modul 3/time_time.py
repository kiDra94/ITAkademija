import time
print(time.time())
miliseconds=round(time.time()*1000)
print(miliseconds)
#zadatka
a = time.time()
for i in range(5):
    print("Hello")
    time.sleep(i)
print(time.time()- a)