import tkinter as tk

class HelloWorld(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(200, 50)
        HelloFrame().pack()

class HelloFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        label = tk.Label(self, text="Hello World", font=("Verdana", 10)).pack(pady=10, padx=10)

HelloWorld().mainloop()