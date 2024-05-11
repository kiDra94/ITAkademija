#importovanje modula
import kivy
#Svaka klasa mora da nasledjuje kivy.app klasu
from kivy.app import App
#Uvodimo kontrolu Label
from kivy.uix.label import Label


#Pravimo klasu koja nasledjuje kivy.app klasu, ona sadrzi metodu build koja vraca labelu
class HelloWorld(App):
    def build(self):
        #Definisemo tekst labele i velicinu slova
        return Label(text="Pera Peric", font_size = 50)
        
#Pokrecemo klasu HelloWorld metodom run
if __name__ == "__main__":
    HelloWorld().run()
