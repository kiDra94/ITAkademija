import tkinter as tk

class HelloWorld(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(200, 50)
        HelloFrame().pack()

class HelloFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        my_var = tk.StringVar(value="My Videos")
        def my_callback(var_name, index, mode):
            print("Traced variable {}, var{}, index{}, mode{}".format(my_var.get(), var_name, index, mode))
                  
        my_var.trace_add('write', my_callback)
        label = tk.Label(self, textvariable = my_var, font=("Verdana", 10)).pack(pady=10, padx=10)
        entry = tk.Entry(self, textvariable = my_var).pack(padx=5, pady=5)

HelloWorld().mainloop()