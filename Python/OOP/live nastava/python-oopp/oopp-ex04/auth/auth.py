import os, getpass
username = input("Username: ")
password = getpass.getpass("Password: ")
os.chdir("oopp-ex04/auth")
f = open("users","r")
l = f.readline()
while l: 
    l = l.strip()
    l = l.split(",")
    if l[0] == username:
        if  l[1] == password:
            print(f"Hello {username}, your current balance is ${l[2]}")
        else:
            print("Your password isn't valid")
        break
    l = f.readline()
else:
    print("No such user")
f.close()