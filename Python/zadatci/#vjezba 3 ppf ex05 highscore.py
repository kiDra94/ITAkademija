#vjezba 3 ppf ex05 highscore
import random
user_score      = int(input("Unesite skor: "))
generated_score = random.randint(0,255)
if user_score > generated_score:
    print("Cestitamo pobjedili ste stari high score! ", generated_score)
    print("Highscore: ", user_score)
else:
    print("Probajte ponovo!", "\n", "Highscore je: ", generated_score)
