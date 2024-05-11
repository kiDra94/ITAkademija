w = 10
h = 5

for i in range(1,w*h+1):
    if i <= w or i > w * h - w or (i % w) == 0 or ((i - 1) % w) == 0:
        print("#",end="")
    else:
        print(" ",end="")
    if (i % w) == 0 :
        print("")