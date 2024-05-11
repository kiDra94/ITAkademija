# ppf ex 08 calc.py
jezici = {"srb":"srpski","en":"english"}
jezik_user = str(input("Chose language (srb;en): "))
for k in jezici:
    if jezik_user == "srb":
        print("Dobar dan izabrali ste srpski jezik!")
        user_prvi_broj = int(input("Unesite prvi broj: "))
        user_drugi_broj = int(input("Unesite drugi broj: "))
        print(f"Zbir od {user_prvi_broj} + {user_drugi_broj} je: ", user_prvi_broj+user_drugi_broj)
        break
    elif jezik_user == "en":
        print("Hello you choose english for your language!")
        user_first_nbr = int(input("Input your 1st numbre: "))
        user_second_nbr = int(input("Input your 2nd numbre: "))
        print(f"The sum of {user_first_nbr} + {user_second_nbr} is: ", user_first_nbr+user_second_nbr)
        break
    else:
        print("Languege not in database!")
        break
