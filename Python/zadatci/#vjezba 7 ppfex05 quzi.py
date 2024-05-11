#vjezba 7 ppfex05 quzi.py
best_game  = "Dota2"
best_phone = "Samsung A54"
best_film  = "Star Wars"
print("Obratite paznju na velika i mala slova!!!")
user_game  = str(input("Koja je najbolja igrica: "))
user_phone = str(input("Koji je najbolji telefon: "))
user_film  = str(input("Koji je najbolji film: "))
print("###############REZULTAT#################")
print("Koja je najbolja igrica: ", "\nOdgovor: ", best_game)
print(best_phone)
print("Koji je najbolji telefon: ", "\nOdgovor: ", best_phone)
print(best_film)
print("Koji je najbolji film: ", "\nOdgovor: ", best_film)
if user_game==best_game and user_phone==best_phone and user_film==best_film:
    print("Osvojili ste 3 poena!")
elif user_game==best_game and user_film==best_film or user_game==best_game and user_phone==best_phone or user_phone==best_phone and user_film==best_film:
    print("Osvojili ste 2 poena!")
elif user_game==best_game or user_film==best_film or user_phone==best_phone:
    print("Osvojli ste 1 poen!")
else:
    print("Osvjili ste 0 poena!")
