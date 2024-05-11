class Dictionary:    
    def get_word(self,word):
        return self.words[word]

class English(Dictionary):
    lang = "English"
    words = {"hello":"Hello","house":"House","car":"Car"}
    
class Deutsch(Dictionary):
    lang = "Deutsch"
    words = {"hello":"Hallo","house":"Haus","car":"Auto"}

while True:
    word = input("Enter word: ")
    dict = English()
    print(f"{dict.lang} : {word}",dict.get_word(word))
    dict = Deutsch()
    print(f"{dict.lang} : {word}",dict.get_word(word))