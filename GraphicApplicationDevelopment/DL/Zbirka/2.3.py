import tkinter as tk

win = tk.Tk()
win.minsize(300, 200)


tk.Label(win,text = 'label1', bg = 'yellow').grid(column = 0, row = 0)
tk.Label(win,text = 'label2',bg = 'green').grid(column = 1, row = 1)
tk.Label(win,text = 'label3', bg = 'red').grid(column = 2, row = 2)
tk.Label(win,text = 'label4',bg = 'blue').grid(column = 3, row = 3)

win.mainloop()