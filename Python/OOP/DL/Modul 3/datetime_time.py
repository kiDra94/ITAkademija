import time
import datetime

date1 = datetime.datetime(2023,11,23,15,38,46)
date2 = datetime.datetime.now()
date3 = datetime.datetime.fromtimestamp(time.time())

print(date1)
print(date2)
print(date3)

entry_time = "2023-02-07 02:43:11"
 
time_obj = datetime.datetime.strptime(entry_time,"%Y-%m-%d %H:%M:%S")
 
print("Entry created in the year",time_obj.year)

print(f"Entry created in {time_obj.year}-{time_obj.month}-{time_obj.day} {time_obj.hour}:{time_obj.minute}:{time_obj.second}")