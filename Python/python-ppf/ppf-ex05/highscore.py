import random 
highscore       = random.randint(0,100)
lasthighscore   = highscore
userscore       = int(input('Enter your score? '))
if(userscore>highscore):
    highscore = userscore
    print("Congrats! You beat the high score", lasthighscore)
else:
    print("You need to practice more")
print("Highscore: ", highscore)
