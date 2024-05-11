import random
print("Enter number?")
u_num   = int(input())
r_num   = random.randint(1,10)
print("Your number", u_num)
print("Computer number", r_num)
print("Hit: ", u_num == r_num)