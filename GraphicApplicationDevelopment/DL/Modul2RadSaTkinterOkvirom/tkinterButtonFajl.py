import tkinter as tk
counter = 0
 
def button_func():
    global counter
    counter +=1
    label_string.set("Button clicked {} times".format(str(counter)))
 
win = tk.Tk()
win.minsize(300, 350)
label_string = tk.StringVar(value = "Button clicked {} times".format(str(counter)))
 
tk.Label(master = win, textvariable = label_string).pack()
tk.Button(master = win, text = 'ClickMe!', command = button_func).pack()
win.mainloop()
