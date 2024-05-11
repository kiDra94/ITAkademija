import os,time
h = 20
w = 20
bx = 7
by = 2
spdx = 1
spdy = 1

while True:
    os.system("clear")
    bx+=spdx
    by+=spdy
    if bx<=0 or bx>=w-1:
        spdx*=-1
    if by<=0 or by>=h-1:
        spdy*=-1 
    for y in range(h):
        for x in range(w): 
            char = " "
            if y==0 or x==0 or y==h-1 or x==w-1:
                char = "#"
            elif y == by and x == bx:
                char = "*"
            print(char,end="")
        print()
    time.sleep(0.1)