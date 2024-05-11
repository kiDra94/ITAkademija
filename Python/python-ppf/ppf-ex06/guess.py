import random
while True:
    score = 0
    num = random.randint(1,11)
    while num != int(input("Guess number? ")):
        score-=1
    print("Game over")    
    print("Negative pts: ",score)
    print("My guessed number: ", num)
    score = 0
