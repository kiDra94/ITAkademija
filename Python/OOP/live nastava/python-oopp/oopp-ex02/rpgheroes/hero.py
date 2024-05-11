from abc import ABC, abstractmethod

class BaseHero(ABC):
    health = 0
    mana = 0
    dead = False
    def areaOfEffectHit(self):
        self.receiveHit()
    @abstractmethod
    def receiveHit(self): pass
    @abstractmethod
    def primaryFire(self): pass
    @abstractmethod
    def secondaryFire(self): pass


