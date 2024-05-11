import kivy
from kivy.app import App
from kivy.uix.label import Label
  
class HelloWorld(App):
    def build(self):
        return Label(text="Hello World", font_size = 100)
         
if __name__ == "__main__":
    HelloWorld().run()