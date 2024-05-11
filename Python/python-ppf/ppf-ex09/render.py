def render(w,h):
    for y in range(h):
        for x in range(w):
            if x==0 or x==w-1 or y==0 or y==h-1:
                print("#",end="")
            else:
                print(" ",end="")
        print()

render(10,10)

