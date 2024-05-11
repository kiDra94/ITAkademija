

from tkinter import *
counter=0
def mouse_click(event):
    global counter
    print('Counter is ',counter)
    counter+=1

window = Tk()
window.minsize(300, 100)
label = Label( window, text="Click here")
label.pack()

#Za Windows
label.bind( "<Double-Button>", mouse_click)

#Za Linux
#label.bind( "<Double-Button-1>", mouse_click)

window.mainloop()
