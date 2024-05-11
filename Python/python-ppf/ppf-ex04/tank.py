dome                = 1
tracks              = 2
motor               = 4

movementMask        = tracks | motor
hitZone             = int(input("Enter hit zone: "))
print("Tank cannot move: ", (movementMask & hitZone) != 0)


