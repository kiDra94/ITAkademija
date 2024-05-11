from tkinter import *
counter = 0

win = Tk()
win.minsize(300, 350)

def button_funcktion(event):
    global counter
    counter +=1
    if counter % 3 ==0:
        print(f"Button clicked 3 times and the count is {int(counter/3)}")

label1 = Label(win, text="Click here 3 times")
label1.pack()
label1.bind("<Button>", button_funcktion)


win.mainloop()