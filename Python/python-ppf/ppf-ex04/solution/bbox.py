x       = 5
y       = 6
width   = 5
height  = 4

userx   = int(input("Enter x : "))
usery   = int(input("Enter y : "))

inZone   = userx >= x and userx <= x + width and usery >= y and usery <= y + height

print("You are in zone: ", inZone)
