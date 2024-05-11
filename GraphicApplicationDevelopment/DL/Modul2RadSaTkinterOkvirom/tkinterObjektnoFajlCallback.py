import tkinter as tk
class HelloFrame(tk.Frame):
    def __init__(self): # self, parent
        tk.Frame.__init__(self) # self, parent
        my_var = tk.StringVar(value = 'Insert text here..') 
 
        def my_callback(var_name, indx, mode): 
            print("Traced variable {}, var{}, indx{}, mode {}".format(my_var.get(), var_name, indx, mode))
         
        my_var.trace_add('write', my_callback) 
        # my_var.set("Insert text here..")
        tk.Label(self, textvariable = my_var).pack(padx = 5, pady = 5) 
        tk.Entry(self, textvariable = my_var).pack(padx = 5, pady = 5)
class HelloWorld(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(300, 200)
        HelloFrame().pack()
        
HelloWorld().mainloop()