from tkinter import *
canvas_width = 300
canvas_height = 300
master = Tk()
master.title("Tkinter Canvas")
tk_canvas = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)

tk_canvas.create_oval(10, 10, 200, 200, outline="black", fill="green", width = 5)
tk_canvas.pack()
master.mainloop()