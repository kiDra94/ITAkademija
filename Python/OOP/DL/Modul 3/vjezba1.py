import time
import datetime
print("What shall I remind you about?")
message = input("Enter message: ")
waittime = input("In how many minutes?: ")

waitime_obj = datetime.datetime.strptime(waittime,"%M") #extract as minutes
wait_time_minutes = waitime_obj.minute #using just the int value from an object

time.sleep(wait_time_minutes*60) #converting minutes to seconds for time.sleep() function

for i in range(5): #repeat code 5 times
    print(message)
    time.sleep(1) # 1 second break between messages