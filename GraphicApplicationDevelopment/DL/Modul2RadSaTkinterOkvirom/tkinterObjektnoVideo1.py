import tkinter as tk

class HelloWorld(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(200, 50)
        tk.Label(self, text="Hello World").pack()


HelloWorld().mainloop()