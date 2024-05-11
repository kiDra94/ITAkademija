import re
while True:
    pattern = re.compile("^[0-9]{3}/[0-9]{3}-[0-9]{4}$")
    phone = input("Enter phone number: ")
    if pattern.search(phone):
        print("Phone is valid")
        break 