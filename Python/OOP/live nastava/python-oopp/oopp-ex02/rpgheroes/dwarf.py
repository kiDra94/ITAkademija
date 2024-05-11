from hero import BaseHero

class DwarfWarrior(BaseHero):
    def receiveHit(self):
        self.health -= 10
        self.dead = self.health <= 0
    def primaryFire(self):
        self.mana -= 5
        print("Firing primary!!!")
    def secondaryFire(self):
        self.mana -= 10
        print("Firing secondary!!!")
    def show(self):
        print(f"Health: {self.health} Mana: {self.mana} Dead: {self.dead}")

