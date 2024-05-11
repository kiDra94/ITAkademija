from tkinter import *
canvas_width = 300
canvas_height = 300
master = Tk()
master.title("Tkinter Canvas")
tk_canvas = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)

tk_canvas.create_arc(50, 50, 200, 200, start = 90,  extent = 180, fill="blue")
tk_canvas.pack()
master.mainloop()