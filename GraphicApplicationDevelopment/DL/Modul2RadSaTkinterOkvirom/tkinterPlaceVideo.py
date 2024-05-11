import tkinter as tk

win = tk.Tk()
win.minsize(300, 100)
tk.Label(win, text="lable1", bg="green").place(x=20, y=10)
tk.Label(win, text="lable2", bg="red").place(x=20, y=30)
tk.Label(win, text="lable3", bg="green").place(x=320, y=10) #nece biti vidljiva, van prozora


win.mainloop()