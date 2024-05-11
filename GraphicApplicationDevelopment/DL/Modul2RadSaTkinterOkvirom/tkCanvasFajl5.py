from tkinter import *
canvas_width = 300
canvas_height = 300
master = Tk()
master.title("Tkinter Canvas")
tk_canvas = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)

points = (0,0,canvas_width/2, canvas_height/2, canvas_width, 0)
id_s = tk_canvas.create_polygon(points, fill = 'green', outline = 'red', width = 5)

tk_canvas.pack()
master.mainloop()