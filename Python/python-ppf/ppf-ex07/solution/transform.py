import math,os,time
M = 10
box = [[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2]] 

translate   = [4,5]
rotate      = 0

while True: 
    translated = []
    rotate+=1
    for x,y in box: 
        an = math.degrees(rotate) 
        dot = [x,y]
        dot[0] = round(dot[0] * math.cos(an) - dot[0] * math.sin(an))
        dot[1] = round(dot[1] * math.sin(an) + dot[1] * math.cos(an))  
        dot[0] += translate[0]
        dot[1] += translate[1] 
        translated.append(dot)

    os.system("clear")

    for y in range(M):
        for x in range(M):
            c = " " 
            if [x,y] in translated:
                c = "#"
            print(c,end="")
        print()
    
    time.sleep(0.5)