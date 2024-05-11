H       = 10
for i in range(H):
    for j in range(H): 
        half = (H-i)/2
        print(" " if j<half or j>H-half else "#" ,end="")
    print()