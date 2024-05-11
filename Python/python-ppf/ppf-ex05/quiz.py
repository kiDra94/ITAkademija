q1 = "Best computer ever? "
q2 = "Best game ever? "
q3 = "Best film ever? "

a1 = "amiga"
a2 = "fallout"
a3 = "matrix" 

pts = 0

if(input(q1)==a1):
    pts+=1
if(input(q2)==a2):
    pts+=1
if(input(q3)==a3):
    pts+=1

print("################### RESULTS ###################") 

print("Question 1: ", q1) 
print("Answer: ", a1)
print("Question 2: ", q2)
print("Answer: ", a2)
print("Question 3: ", q3)
print("Answer: ", a3)
print("Your earned points: ", pts)