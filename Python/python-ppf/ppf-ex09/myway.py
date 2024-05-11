def render(w,h,path=[]): 
    for y in range(h):
        for x in range(w): 
            pt = " "
            if x==0 or x==w-1 or y==0 or y==h-1:
                pt = "#" 
            elif [x,y] in path:
                pt = "@"
            print(pt,end="")
        print()

def path(start,end):
    res = [start.copy()]
    while True: 
        lastpt = res[len(res)-1]
        newpt = lastpt.copy()
        if lastpt[0] < end[0]:
            newpt[0]+=1
        if lastpt[1] < end[1]:
            newpt[1]+=1
        if newpt == lastpt:
            break
        res.append(newpt)
    return res
        

render(20,15,path([2,3],[17,12])) 



