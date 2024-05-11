import time
gmt = time.gmtime()
print("Current date is: ",gmt.tm_mday,gmt.tm_mon,gmt.tm_year)
gmt = time.gmtime(631152000)
print("Current date is: ",gmt.tm_mday,gmt.tm_mon,gmt.tm_year)
while True:
    print("Exact time is: ")
    my_time = time.localtime(time.time())
    print(my_time.tm_hour,"hours",my_time.tm_min,"minutes")
    if my_time.tm_min in [15, 30, 0]:
        break
    time.sleep(60)
