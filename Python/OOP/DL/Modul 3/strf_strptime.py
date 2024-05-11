import time
print("Exact date is: ")
my_time = time.localtime(time.time())
my_time_parsed = time.strftime("Month: %b Day %d Year: %Y",my_time)
print(my_time_parsed)
time.sleep(60)

entry_time = "2023-02-07 02:43:11"
 
time_obj = time.strptime(entry_time,"%Y-%m-%d %H:%M:%S")
print("Entry created in the year",time_obj.tm_year)
