import tkinter as tk
win = tk.Tk()
win.minsize(300, 200)

tk.Label(win,text = 'label1', bg = 'red').place(y = 10, x = 20)
tk.Label(win,text = 'label2',bg = 'blue').place(y=10 , x = 150)
win.mainloop()
