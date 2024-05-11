import game
import random
class gamble(game.game): 
    def pick(self): 
        number = random.randint(1,100)
        print(f"Number is {number}")
        userchoice = self.get_user_input("Greater(1)/Smaller(2)/Equals(3): ")
        newnumber = random.randint(1,100);
        if userchoice!=1 and userchoice!=2 and userchoice!=3:
            print("Wrong entry")
            return
        if userchoice==1 and newnumber>number:
            print(f"Correct ({newnumber})")
        elif userchoice==2 and newnumber<number:
            print(f"Correct ({newnumber})")
        elif userchoice==3 and newnumber==number:
            print(f"Correct ({newnumber})")
        else:
            print(f"Incorrect ({newnumber})")


