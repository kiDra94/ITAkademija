import tkinter as tk
win = tk.Tk()
win.minsize(300, 100)
tk.Label(win,text = 'label1', bg = 'green').pack(side = tk.LEFT,  fill = tk.BOTH)
tk.Label(win,text = 'label2',bg = 'red').pack(fill = tk.BOTH)
tk.Label(win,text = 'label3',bg = 'purple').pack(expand=True, fill = tk.BOTH)
win.mainloop()