from tkinter import *
from tkinter import messagebox

def mouse_click(event):
    print("Click event")

def mouse_click1(event):
    print("Click event at x={}, y={}".format(event.x, event.y))

def mouse_scroll(event):
    print("Mouse event at x={}, y={}".format(event.x, event.y))
    print("Event source widget: {}".format(event.widget))
    print("Event type: {}".format(event.type))

def confirm_exit():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

window = Tk()
label = Label(window, text="Click here")
label.pack()
label.bind("<Button>", mouse_click)

label1 = Label(window, text="Click here1")
label1.pack()
label1.bind("<Double-Button>", mouse_click1)

label2 = Label(window, text="Click here")
label2.pack()
label2.bind( "<MouseWheel>", mouse_scroll)

window.protocol("WM_DELETE_WINDOW", confirm_exit)



window.mainloop()