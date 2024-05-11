import enum
import random
import math

class PlayerType(enum.Enum):
    Man             = 1
    Computer        = 2

class GameStates(enum.Enum):
    Uninitialized   = 1
    Running         = 2
    Finished        = 3

class Point:
    def __init__(self,x,y):
        self.x      = x
        self.y      = y

class GamePlay:

    def __init__(self, matrix_size):
        self.gamestate = GameStates.Uninitialized
        self.trajectory = []
        self.matrix_size = matrix_size
        self.shoots = 0
        self.user = None
        self.computer = None

    def addPlayer(self,ptype,x=0,y=0):
        if ptype == PlayerType.Man:
            self.user = Point(x,y)
        else: 
            self.computer = Point(random.randint(1,self.matrix_size-2),random.randint(1,self.matrix_size-2))
            self.gamestate = GameStates.Running
        # switch(ptype){
        #     case Man:
        #         user = new Point(x,y); 
        #     break;
        #     case Computer:
        #         Random r = new Random();
        #         computer = new Point(r.nextInt(matrix_size-2)+1,r.nextInt(matrix_size-2)+1);
        #         gamestate = GameStates.Running;
        #     break;
        # }
    def reset(self):
        self.shoots = 0;
        self.trajectory.clear()
        self.gamestate = GameStates.Uninitialized; 

    def shoot(self,angle,trgt):
        source = None
        target = None
        #Point source , target;
        if trgt == PlayerType.Computer:
            self.shoots+=1;
            source = self.user;
            target = self.computer;
        else:
            source = self.computer;
            target = self.user;

        radians = math.radians(angle)
        speed = 1;
        x = source.x
        y = source.y;
        self.trajectory.clear();
        self.trajectory.append(Point(int(x),int(y)))
        counter = 0
        while True:
            x+=speed*math.cos(radians);
            y+=speed*math.sin(radians); 
            if(int(x)==target.x and int(y)==target.y):
                self.gamestate = GameStates.Finished
                return True
            if int(x)<=0 or int(x)>self.matrix_size or int(y)<0 or int(y)>self.matrix_size:
                return False;
            self.trajectory.append(Point(int(x),int(y)))

    def draw(self):
        c = range(self.matrix_size)
        for h in c:
            for w in c:
                if self.user and h == self.user.y and w == self.user.x:
                    print("U",end="")
                elif self.computer and h == self.computer.y and w == self.computer.x:
                    print("C",end="")
                else:
                    if h==0 or h == self.matrix_size-1 or w==0 or w == self.matrix_size-1:
                        print("O",end="")
                    else:
                        point_draw = True
                        for pt in self.trajectory: 
                            if pt.x == w and pt.y == h:
                                print("*",end="")
                                point_draw = False
                        if point_draw:
                            print(" ",end="")
            print()