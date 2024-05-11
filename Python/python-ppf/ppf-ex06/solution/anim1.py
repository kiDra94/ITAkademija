import time
target  = 50
x       = 1
dir     = 1
while True:
    print("\r",end="")
    j = 0
    while j < target:
        print("#" if x==j else " ",end="")
        j+=1
    if x==0 or x==target:
        dir*=-1
    x+=dir
    time.sleep(0.05)