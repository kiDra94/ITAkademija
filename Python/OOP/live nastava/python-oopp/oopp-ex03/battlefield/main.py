import battlefield
import time
import random
gameplay = battlefield.GamePlay(20)   
while True: 
    plx = int(input("Enter position x: "))
    ply = int(input("Enter position y: "))
    gameplay.addPlayer(battlefield.PlayerType.Man, plx, ply)
    gameplay.addPlayer(battlefield.PlayerType.Computer)
    gameplay.draw()
    
    while True: 
        angle = int(input("Enter angle: ")) 
        hit = gameplay.shoot(angle,battlefield.PlayerType.Computer)
        gameplay.draw()
        if hit:
            print("You HIT computer")
        else:
            print("Miss. Computer turn")
            time.sleep(2)
            compangle =  random.randint(0,360)
            hit = gameplay.shoot(compangle,battlefield.PlayerType.Man)
            gameplay.draw()
            print(f"Computer angle {compangle}")
            if hit:
                print("Computer HIT you, you lose!")
                
        if gameplay.gamestate == battlefield.GameStates.Finished:
            break 

    print("*************************************")
    print(f"Total shots\t{gameplay.shoots}")
    print("*************************************")
    another_game = input("Another game (y/n)?")
    if another_game == "n":
        break
    else:
        gameplay.reset()