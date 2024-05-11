import os 
import time
import math
w = 30
h = 15

ptx = 5.0
pty = 5.0 

offsetx = 15
offsety = 7

alpha = 0.3

while True:
    #Update

    nptx = (math.cos(alpha) * ptx) + (-math.sin(alpha) * pty)
    npty = ((math.sin(alpha)) * ptx) + (math.cos(alpha) * pty)

    ptx = nptx
    pty = npty
     
    #Render
    os.system("clear")
    for y in range(h):
        for x in range(w):
            ptdrawn = False
            if  x == 0 or y == 0 or x == w-1 or y == h-1 or (x == int(ptx) + offsetx and y == int(pty) + offsety):
                print("#",end="")
                ptdrawn = True
            if not ptdrawn:
                print(" ",end="")
        print("")
    time.sleep(0.05)