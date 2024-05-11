class Body:
    weight      = 0
    friction    = 0
    speed       = 0
    def __str__(self):
        return f"w: {self.weight} f: {self.friction} s: {self.speed}"

class BodyBuilder:
    def __init__(self):
        self.body = Body()
    
    def applyWeight(self,w):
        self.body.weight = w
        return self
    
    def applyFriction(self,f):
        self.body.friction = f
        return self
    
    def applySpeed(self,s):
        self.body.speed = s
        return self

    def build(self):
        return self.body

b = BodyBuilder().applyFriction(0.2).applySpeed(4.5).applyWeight(8).build()
print(b)

