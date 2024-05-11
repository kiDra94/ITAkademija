class Dictionary:    
    def get_word(self,word):
        return self.words[word] #return entered word

class English(Dictionary): #language and word list
    lang = "English"
    words = {"hello":"Hello","house":"House","car":"Car"}
    
class Deutsch(Dictionary): #language and word list
    lang = "Deutsch"
    words = {"hello":"Hallo","house":"Haus","car":"Auto"}

while True:
    word = input("Enter word: ")
    dict = English() 
    print(dict.lang, word, dict.get_word(word)) #show language chosen word inserted and word from dictionary
    dict = Deutsch()
    print(dict.lang, word, dict.get_word(word))