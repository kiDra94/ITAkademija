import os, time, random, math

class Projectile:
    x = 0
    y = 0
    angle = 0
    power = 0

class Target:
    x = 0
    y = 0  

class Game:  

    angle_offset = math.radians(90)
    hit_offset  = 2
    
    def __init__(self):
        self.target = Target()
        self.w = 50
        self.h = 30
        self.proj = Projectile()
        self.proj.x = self.w / 2
        self.proj.y = self.h - 2

    def update(self,reset=False):
        if reset:
            self.proj.x = self.w / 2
            self.proj.y = self.h - 2
            return
        self.proj.x += self.proj.power * math.cos(self.proj.angle-Game.angle_offset)
        self.proj.y += self.proj.power * math.sin(self.proj.angle-Game.angle_offset)

    def render(self):
        for y in range(self.h):
            for x in range(self.w):
                point_drawn = False
                if x == int(self.proj.x) and y == int(self.proj.y):
                    print("@",end="") 
                    continue
                if self.target.x == x and self.target.y == y:
                    print("T",end="")
                    continue
                if y == self.h-1:
                    print("#",end="")
                else:
                    print(" ",end="")
            print()
        
    def check_collission(self):
            return self.proj.x >= self.target.x - Game.hit_offset and self.proj.x <= self.target.x + Game.hit_offset and self.proj.y >= self.target.y - Game.hit_offset and self.proj.y <= self.target.y + Game.hit_offset

    def check_out_of_bounds(self):
            return self.proj.x <= 0 or self.proj.y <= 0 or self.proj.x >= self.w 

    def set_angle(self):
        angle = math.radians(float(input("angle: "))) 
        self.proj.angle = angle 

    def start(self):

        while True:
            self.target.x = random.randint(0,self.w)
            self.target.y = random.randint(0,self.h-10) 

            self.update(True)
            os.system("cls") 
            self.render() 

            self.set_angle() 
            self.proj.power = 0.2

            while True:
                self.update()
                os.system("cls") 
                self.render()

                if self.check_collission():
                    print("You hit the target!")
                    time.sleep(5)
                    break

                if self.check_out_of_bounds():
                    print("You missed")
                    time.sleep(5)
                    break

                time.sleep(0.01)
                
game = Game()
game.start()