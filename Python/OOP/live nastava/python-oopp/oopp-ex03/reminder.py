import time

message = input("Enter message: ")
waittime = int(input("Enter time: "))

for i in range(waittime):
    remaining = waittime - i
    print(f"\rTime remaining: {remaining}",end="")
    time.sleep(1)

print()

for i in range(10):
    print(message)
    time.sleep(1)