H       = 10
x       = 1
for i in range(H*2):
    for j in range(x):
        print("#",end="") 
    x = x + 1 if i < H-1 else x - 1
    print("")

