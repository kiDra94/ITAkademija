from tkinter import *
import globals as gl

def click_me_event():
    myLabel = gl.GlobalComponents.get("myLabel")
    myEntry = gl.GlobalComponents.get("myEntry")
    myLabel["text"] = myEntry.get()

window = Tk()
window.title("My first app")
window.geometry("600x400")
window.iconbitmap("./python.ico")

myLabel = Label(window, text="Hello World", 
                font=("Arial", 20), background="pink",
                foreground="blue",
                width=28, height=5, anchor="center")
gl.GlobalComponents.set("myLabel", myLabel)

myButton = Button(window, text="Click Me!", font=("Arial", 20),
                  command=click_me_event)

myEntry = Entry(window, show="*", font=("Arial", 20))
gl.GlobalComponents.set("myEntry", myEntry)
myEntry.pack()
myLabel.pack()
myButton.pack()

if __name__ == "__main__":
    window.mainloop()