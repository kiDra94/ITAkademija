import datetime

first_entry_date = "2023-02-07 02:43:11"
last_entry_date = "2023-08-07 03:46:01"

first_entry_obj = datetime.datetime.strptime(first_entry_date,"%Y-%m-%d %H:%M:%S")

last_entry_obj = datetime.datetime.strptime(last_entry_date,"%Y-%m-%d %H:%M:%S")

activity = last_entry_obj - first_entry_obj
print("User was active for: ",activity.days,"days")
