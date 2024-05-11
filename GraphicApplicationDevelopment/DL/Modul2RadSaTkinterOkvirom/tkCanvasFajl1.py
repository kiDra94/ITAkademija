from tkinter import *
canvas_width = 300
canvas_height = 300
master = Tk()
master.title("Tkinter Canvas")
tk_canvas = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
tk_canvas.create_line(10, 20, 200, 10)
tk_canvas.create_line(250, 10, 250, 290, dash=(8, 4))
tk_canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85, width = 5)
tk_canvas.pack(expand = YES, fill = BOTH)

tk_canvas.create_arc(50, 50, 200, 200, start = 90,  extent = 180, fill="blue")
tk_canvas.pack()
master.mainloop()