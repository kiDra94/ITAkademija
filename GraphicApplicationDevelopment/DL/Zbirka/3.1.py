import tkinter as tk
root=tk.Tk()
width=400
height=400
canvas=tk.Canvas(root,width=400,height=400)
canvas.pack()

line=canvas.create_line(100, 10, 300, 10,fill="red")

def redraw():
    current_coords = canvas.coords(line)
    if (current_coords[1]>=height):
            root.after(1, root.destroy)
    canvas.move(line,0,5)

    canvas.after(50,redraw)
redraw()

root.mainloop()
