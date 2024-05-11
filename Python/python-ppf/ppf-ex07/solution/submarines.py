m           = 10
submarines  = [3,5,3,6,7,6,8,6,2,1,2,2] 
subs        = len(submarines) 
for y in range(m):
    for x in range(m):
        char = " "
        if x==0 or x==m-1 or y==0 or y==m-1:
            char = "#"
        else:
            i = 0 
            while i<subs:
                x1,y1,x2,y2 = submarines[i:i+4]
                if (x1==x and y1==y) or (x2 == x and y2 == y):
                    char = str(round((i/4)+1))
                    break
                i+=4
        print(char,end="") 
    print()

