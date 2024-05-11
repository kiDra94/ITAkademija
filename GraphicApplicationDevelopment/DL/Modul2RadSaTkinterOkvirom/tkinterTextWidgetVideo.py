import tkinter as tk
counter = 0

win = tk.Tk()
win.minsize(300, 350)

def button_funcktion(text_widget):
    global counter
    counter +=1
    text_widget.delete("1.0", tk.END)
    text_widget.insert("1.0", "Button clicked {} times".format(str(counter)))

text_widget = tk.Text(master=win)
text_widget.pack()

tk.Button(master=win, text="Clicke me", command= lambda: button_funcktion(text_widget)).pack()



win.mainloop()