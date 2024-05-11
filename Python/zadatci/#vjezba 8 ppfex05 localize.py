#vjezba 8 ppfex05 localize.py
import langid
user_lang = str(input("Unesite jezik: "))
guten_tag = "de"
good_day  = "en"
dobar_dan = "srb"
if user_lang == "de":
    print("Guten Tag")
elif user_lang == "en":
    print("Good day")
elif user_lang == "srb":
    print("Dobar dan")
else:
    print("Jezik nije u bazi!")
