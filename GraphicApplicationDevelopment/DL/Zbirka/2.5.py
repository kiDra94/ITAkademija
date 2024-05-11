import tkinter as tk
counter1 = 0
counter2 = 0

def button1_func():
    global counter1
    if counter1==10:
        counter1=0
    counter1 +=1
    label_string1.set("Button1 clicked {} times".format(str(counter1)))
    
def button2_func():
    global counter2
    if counter2==10:
        counter2=0
    counter2 +=1
    label_string2.set("Button2 clicked {} times".format(str(counter2)))
    
    


win = tk.Tk()
win.minsize(300, 350)
label_string1 = tk.StringVar(value = "Button1 clicked {} times".format(str(counter1)))
label_string2 = tk.StringVar(value = "Button2 clicked {} times".format(str(counter2)))


tk.Label(master = win, textvariable = label_string1).pack()
tk.Button(master = win, text = 'ClickMe!', command = button1_func).pack()

tk.Label(master = win, textvariable = label_string2).pack()
tk.Button(master = win, text = 'ClickMe!', command = button2_func).pack()
win.mainloop()
