import tkinter as tk
counter = 0
def button_func(text_lines):
    global counter
    counter +=1
    text_lines.insert(tk.END, "Button clicked {} times\n".format(str(counter)))

win = tk.Tk()
win.minsize(300, 350)
boolean_var = tk.BooleanVar(win)

tk.Label(text = 'List items:').pack()
text_lines = tk.Listbox(master = win, width = 30)

text_lines.pack()
tk.Button(master = win, text = 'ClickMe!', command = lambda: button_func(text_lines)).pack()

win.mainloop()
