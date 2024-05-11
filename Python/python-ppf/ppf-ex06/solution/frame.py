import os 
import time
w = 30
h = 15

while True:
    os.system("clear")
    for y in range(h):
        for x in range(w):
            print("#",end="")
        print("")
    time.sleep(0.1)