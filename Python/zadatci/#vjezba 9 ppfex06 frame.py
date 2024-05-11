#vjezba 9 ppfex06 frame
import os
import time
h = 20
w = 15
x = 0
while True:
    os.system("clear")
    for x in range(h):
        for y in range(w):
            print("#", end="")
        print("")
    time.sleep(0.1)
