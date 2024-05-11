from tkinter import * 
import tkinter.messagebox as messagebox
import globals as gl

def choose_event():
    choices = {
        "1": "A fine meal",
        "2": "A nice bath",
        "3": "A picnic in the valley",
        "0": "Not selected"
    }
    
    choice1 = gl.GlobalValues.get("choice1")
    choice2 = gl.GlobalValues.get("choice2")
    choice3 = gl.GlobalValues.get("choice3")
    messagebox.showinfo("Choices", 
f"""Choices:
Choice 1: {choices[str(choice1.get())]}
Choice 2: {choices[str(choice2.get())]}
Choice 3: {choices[str(choice3.get())]}""")

window = Tk()
window.title("Choices")
window.geometry("350x250")
DEFAULT_FONT = ("Arial", 20)

choice1 = IntVar()
choice2 = IntVar()
choice3 = IntVar()
gl.GlobalValues.set("choice1", choice1)
gl.GlobalValues.set("choice2", choice2)
gl.GlobalValues.set("choice3", choice3)


chkChoice1 = Checkbutton(window, font=DEFAULT_FONT, text="Option 1",
                         onvalue=1, offvalue=0, variable=choice1)
chkChoice2 = Checkbutton(window, font=DEFAULT_FONT, text="Option 2",
                         onvalue=2, offvalue=0, variable=choice2)
chkChoice3 = Checkbutton(window, font=DEFAULT_FONT, text="Option 3",
                         onvalue=3, offvalue=0, variable=choice3)
btnChoose = Button(window, font=DEFAULT_FONT, text="Choose",
                   command=choose_event)

chkChoice1.pack()
chkChoice2.pack()
chkChoice3.pack()
btnChoose.pack()

if __name__ == "__main__":
    window.mainloop()