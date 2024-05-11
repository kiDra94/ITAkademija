import tkinter as tk
  
win = tk.Tk()
win.minsize(300, 100)
 
win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=2)
  
tk.Label(win,text = 'label1', bg = 'green').grid(column = 0, row = 0, sticky = 'E')
tk.Label(win,text = 'label2',bg = 'red').grid(column = 1, row = 0, sticky = 'W')

win.mainloop()