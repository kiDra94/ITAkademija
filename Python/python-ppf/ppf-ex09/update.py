import math,time
speed   = 1
angle   = 0
px      = 0
py      = 0
width   = 20
height  = 15 

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

def update():
    global px,py
    an = math.radians(angle)
    px+=speed * math.cos(an)
    py+=speed * math.sin(an)

def path(tx,ty):
    global angle 
    pts = []
    while (tx,ty) != (int(px),int(py)): 
        angle = math.degrees(math.atan2(ty-py,tx-px))
        update()
        pts.append([int(px),int(py)])  
    return pts

render(width,height,path(15,4))

