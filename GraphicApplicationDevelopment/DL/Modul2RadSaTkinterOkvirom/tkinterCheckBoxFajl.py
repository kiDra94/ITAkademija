import tkinter as tk
root = tk.Tk()
var = tk.BooleanVar()
var1 = tk.BooleanVar()
chk = tk.Checkbutton(root, text='Male', variable=var)
chk.pack()
chk1 = tk.Checkbutton(root, text='Female', variable=var1)
chk1.pack()
tk.mainloop()