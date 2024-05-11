import tkinter as tk
counter = 0

win = tk.Tk()
win.minsize(300, 350)

def button_funcktion():
    global counter
    counter +=1
    label_string.set("Button clicked times {}".format(str(counter)))

label_string = tk.StringVar(value="Button clicked times {}".format(str(counter)))

tk.Label(master=win, textvariable=label_string).pack()
tk.Button(master=win, text="Clicke me", command=button_funcktion).pack()



win.mainloop()