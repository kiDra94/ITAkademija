import os, time, random

class Ticket:
    def __init__(self,name,numbers):
        self.name = name
        self.numbers = numbers

class Bingo:  
    def __init__(self):
        self.round = 0
        self.numbers = []
        self.tickets = []

    def enter_numbers(self):
        while True:
            print("Entering ticket: ")
            username = input("Your name: ")
            numbers = input("Numbers (x,y,z..): ")
            if not username or not numbers:
                print("No tickets entered")
                break
            else:
                self.tickets.append(Ticket(username,list(map(int,numbers.split(",")))))

    def check_results(self):
        hasWinner = False
        for ticket in self.tickets:
            #intersection = []
            intersection = [value for value in ticket.numbers if value in self.numbers]
            #for number in self.numbers:
                #if number in ticket.numbers:
                    #intersection.append(number)
            if len(intersection) > 0:
                hasWinner = True
                if len(intersection) == len(self.numbers):
                    print(f"User {ticket.name} has BINGO")
                else:
                    print(f"User {ticket.name} hit numbers: {intersection}")
        if not hasWinner:
            print("We don't have winner for this round")

    def start(self):
        self.round = 0
        while True:
            os.system("cls")
            self.round+=1 
            print(f"Round: {self.round}")
            self.numbers.clear()
            self.tickets.clear()
            self.enter_numbers()
            self.numbers = random.sample(range(1, 11), 5)
            print(f"Starting draw...")
            for i in range(5):
                time.sleep(1)
                print(self.numbers[i],end=" ")
            print()
            self.check_results()
            time.sleep(10)
            
bingo = Bingo()
bingo.start()