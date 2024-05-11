import tkinter as tk
 
class HelloFrame(tk.Frame):
    def __init__(self): 
        tk.Frame.__init__(self) 
        my_var = tk.StringVar(value = 'Insert text here...') 
        my_var.set("Insert text here!!!")
        tk.Label(self, textvariable = my_var).pack(padx = 5, pady = 5)
        tk.Entry(self, textvariable = my_var).pack(padx = 5, pady = 5)
        
class HelloWorld(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(300, 200)
        HelloFrame().pack()
        
HelloWorld().mainloop()