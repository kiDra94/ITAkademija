from tkinter import * 
import tkinter.messagebox as messagebox
import globals as gl

def choose_event():
    rbValue = gl.GlobalValues.get("rbValue")
    if rbValue.get() == "1":
        messagebox.showinfo("Option 1", "You chose first option.")
    elif rbValue.get() == "2":
        messagebox.showinfo("Option 2", "You chose second option.")
    elif rbValue.get() == "3":
        messagebox.showinfo("Option 3", "You chose third option.")

window = Tk()
window.title("Choices")
window.geometry("350x250")
DEFAULT_FONT = ("Arial", 20)

rbValue = StringVar(value="1")
gl.GlobalValues.set("rbValue", rbValue)
rbOption1 = Radiobutton(window, text="Option 1", value="1",
                        variable=rbValue, font=DEFAULT_FONT)
rbOption2 = Radiobutton(window, text="Option 2", value="2",
                        variable=rbValue, font=DEFAULT_FONT)
rbOption3 = Radiobutton(window, text="Option 3", value="3",
                        variable=rbValue, font=DEFAULT_FONT)
lblOption = Label(window, textvariable=rbValue, font=DEFAULT_FONT)
btnChoose = Button(window, text="Choose option", font=DEFAULT_FONT,
                   command=choose_event)

rbOption1.pack()
rbOption2.pack()
rbOption3.pack()
lblOption.pack()
btnChoose.pack()


if __name__ == "__main__":
    window.mainloop()