import game
import random
class blackred(game.game): 
    def pick(self):
        userchoice = self.get_user_input("Red(1)/Black(2)? ")
        number = random.randint(1,100)
        if userchoice!=1 and userchoice!=2:
            print("Wrong entry")
            return; 
        if number>=50 and userchoice==1:
            print("Correct (Red)")
        elif number<50 and userchoice==2:
            print("Correct (Black)")
        else:
            msg = "Black" if number < 50 else "Red"
            print(f"Incorrect ({msg})")