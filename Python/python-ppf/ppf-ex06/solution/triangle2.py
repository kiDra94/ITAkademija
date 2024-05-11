H       = 10
for i in range(H):
    for j in range(H):
        print(" " if j<i else "#",end="")            
    print()