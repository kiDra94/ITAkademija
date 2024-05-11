import tkinter as tk
win = tk.Tk()
win.minsize(300, 200)

tk.Label(win,text = 'labela1', bg = 'yellow').pack(expand=True,side = tk.LEFT,  fill = tk.BOTH)
tk.Label(win,text = 'labela2',bg = 'green').pack(expand=True,side = tk.LEFT, fill = tk.BOTH)
tk.Label(win,text = 'labela3',bg = 'blue').pack(expand=True,side = tk.LEFT, fill = tk.BOTH)


fill = tk.BOTH
win.mainloop()
