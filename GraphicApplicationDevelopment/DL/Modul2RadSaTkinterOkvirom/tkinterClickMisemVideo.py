from tkinter import *

def mouse_click(event):
    print("Click event")

def mouse_click1(event):
    print("Click event at x={}, y={}".format(event.x, event.y))

def exit_w():
    print("Exit")
    window.destroy()

window = Tk()
label = Label(window, text="Click here")
label.pack()
label.bind("<Button>", mouse_click)

label1 = Label(window, text="Click here1")
label1.pack()
label1.bind("<Double-Button>", mouse_click1)

window.protocol("WM_DELETE_WINDOW", exit_w)

window.mainloop()