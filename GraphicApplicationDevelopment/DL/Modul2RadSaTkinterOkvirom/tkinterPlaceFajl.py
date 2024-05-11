import tkinter as tk
win = tk.Tk()
win.minsize(300, 100)
tk.Label(win,text = 'label1', bg = 'green').place(x = 20, y = 10)
tk.Label(win,text = 'label2',bg = 'red').place(x = 20, y = 30)
win.mainloop()