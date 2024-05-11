import random
class Airplane:  
    def __init__(self,name,health,ammo):
        self.name   = name
        self.health = health
        self.ammo   = ammo
    def shoot(self,target):
        am = random.randint(0,10)
        target.health -= am * 2
        self.ammo -= am
        return self.ammo <= 0 or self.health <= 0


il = Airplane("Ilyushin",100,100)
sf = Airplane("Spitfire",100,100)
airplanes = (il,sf)

print(f"round\tname      \thealth/ammo\t:\tname      \thealth/ammo")
print(f"***************************************************************************")
round = 0
while True:
    round+=1
    finished = False
    for i in range(len(airplanes)):
        a1 = airplanes[abs(i-1)]
        a2 = airplanes[i]
        if a1.shoot(a2):
            finished = True
    print(f"{round}\t{a1.name}\t{a1.health}/{a1.ammo}\t\t\t{a2.name}\t{a2.health}/{a2.ammo}")
    if finished:
        break