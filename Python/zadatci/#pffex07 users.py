#pffex07 users
blacklist = ["Jovan", "Simo", "Ana"]
users = []
while True:
    user_input = str(input("Unesite ime: "))
    if user_input in blacklist:
        print("Pristup nije dozvoljen")
    else:
        users.append(user_input)
        print("Trenutni korisnik: ", users)