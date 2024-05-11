import tkinter as tk

class Okvir(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        label = tk.Label(self, text="Pera Peric", 
        font=("Ariel", 15)).pack(pady=50, padx=20)    
        
        
        
class Prozor(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(500, 200) 
        Okvir().pack()
        
Prozor().mainloop()
