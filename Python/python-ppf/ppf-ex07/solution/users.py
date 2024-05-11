blacklist = ["peter","john","sally"]
users = []
while True:
    newuser = input("Username: ")
    if newuser in blacklist:
        print("Sorry, you cannot enter")
    else:
        users.append(newuser)
    print("Current users:")
    print(users)