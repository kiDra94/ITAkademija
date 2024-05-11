# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry (widthxheight)
root.geometry('350x200')

#adding a lable to the root window
lbl = Label(root, text="Are you a Geek?")
lbl2 = Label(root, text="Are you a Geek?")
'''lbl.grid() #gore lijevo
lbl2.grid()'''
lbl.pack()
lbl2.pack()

# all widgets will be here
# Execute Tkinter
root.mainloop()

