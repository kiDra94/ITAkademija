import tkinter as tk
counter = 0
def button_func(text_widget,text_lines):
    global counter
    counter +=1
    text_widget.delete("1.0", tk.END)
    text_widget.insert("1.0","Button clicked {} times\n".format(str(counter)))
    text_lines.insert(tk.END, "Button clicked {} times\n".format(str(counter)))
win = tk.Tk()
win.minsize(300, 350)
  
 
tk.Label(text = 'Text box:')
text_widget = tk.Text(master = win, height = 5,width =25)
  
text_widget.pack()
tk.Label(text = 'List items:').pack()
text_lines = tk.Listbox(master = win, width = 30)
  
text_lines.pack()
tk.Button(master = win, text = 'ClickMe!', command = lambda:button_func(text_widget, text_lines)).pack()
  
win.mainloop()