import os, time, random

class Team:
    def __init__(self,name):
        self.name = name

class Score:
    home = 0
    away = 0

class Match: 
    def __init__(self,t1,t2):
        self.home = t1
        self.away = t2
        self.minute = 0
        self.score = Score()
    def getGoals(self):
        return random.randint(1,10) == 5, random.randint(1,10) == 5
    def start(self):
        self.minute = 0
        while True:
            os.system("cls")
            print(f"{self.home.name} vs {self.away.name}") 
            g1, g2 = self.getGoals()
            self.score.home += 1 if g1 else 0
            self.score.away += 1 if g2 else 0
            self.print_score()
            self.minute += 1
            time.sleep(0.2)
            if self.minute > 90:
                print("Match ended")
                exit()
    def print_score(self):
        print(f"{self.score.home} - {self.score.away} ({self.minute} minute)")
        
t1 = Team("Manchester United")
t2 = Team("Chelsea")

match = Match(t1,t2)
match.start()