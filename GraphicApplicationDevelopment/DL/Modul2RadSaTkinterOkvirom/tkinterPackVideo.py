import tkinter as tk

win = tk.Tk()
win.minsize(300, 100)
tk.Label(win, text="lable1", bg="green").pack(fill=tk.BOTH, expand=True)
tk.Label(win, text="lable2", bg="red").pack(fill=tk.BOTH, expand=True)


win.mainloop()