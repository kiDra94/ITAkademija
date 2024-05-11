class Grid():

    def __init__(self,w,h):
        self.target_x = 0
        self.target_y = 0
        self.start_x = 0
        self.start_y = 0
        self.w = w
        self.h = h 
        self.path = []
        self.wall = ()

    def set_wall(self,wall):
        self.wall = wall
    
    def render(self):
        for y in range(self.h):
            for x in range(self.w): 
                spr = " "
                if (x,y) in self.path:
                    spr = 'O'
                elif (x,y) == (self.start_x,self.start_y):
                    spr = "S"
                elif (x,y) == (self.target_x,self.target_y):
                    spr = "T"
                elif (x,y) in self.wall:
                    spr = "#"
                print(spr,end="")
            print()
    
    def set_target(self,x,y):
        self.target_x = x
        self.target_y = y

    def set_start(self,x,y):
        self.start_x = x
        self.start_y = y

    def calculate_path(self):
        next = g.get_next_point(g.start_x,g.start_y)
        self.path.append(next)  
        while next != (g.target_x,g.target_y):
            prev = next
            next = g.get_next_point(prev[0],prev[1])
            if prev == next:
                break
            self.path.append(next)  

    def get_next_point(self,x,y):
        neighbours = ((x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1))
        candidate = (self.w,self.h)
        for px,py in neighbours: 
            if (px,py) in self.wall or (px,py) in self.path:
                continue
            if (abs(self.target_x - px) + abs(self.target_y - py)) < (abs(self.target_x - candidate[0]) + abs(self.target_y - candidate[1])):
                candidate = (px,py)
        return candidate
        print("Getting best candidate")

g = Grid(30,20)
g.set_wall(((10,5),(10,6),(10,7),(10,8),(10,9),(10,10),(10,11),(10,12),(10,13),(10,14),(10,15)))
g.set_start(0,10)
g.set_target(15,10)
g.calculate_path()
g.render() 