import tkinter as tk

root_window = tk.Tk()
root_window.minsize(200, 50)

lable = tk.Label(root_window, text="Hello World")
lable.pack() #prikazuje

root_window.mainloop() # stavlja u beskonacnu petlju da se vidi

