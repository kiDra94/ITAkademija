import tkinter as tk
counter = 0
 
def button_func(text_widget):
    global counter
    counter +=1
    text_widget.delete("1.0", tk.END)
    text_widget.insert("1.0","Button clicked {} times".format(str(counter)))
 
win = tk.Tk()
win.minsize(300, 350)
 
text_widget = tk.Text(master = win)
text_widget.pack()
tk.Button(master = win, text = 'ClickMe!', command = lambda: button_func(text_widget)).pack()
win.mainloop()