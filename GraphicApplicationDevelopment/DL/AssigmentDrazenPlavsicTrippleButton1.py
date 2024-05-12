from tkinter import *
counter = 0

win = Tk()
win.minsize(300, 350)

def button_funcktion(event):
    global counter
    counter +=1
    print(f"Button clicked 3 times and the count is {counter}")

label1 = Label(win, text="Click here 3 times")
label1.pack()
label1.bind("<Triple-Button>", button_funcktion)


win.mainloop()