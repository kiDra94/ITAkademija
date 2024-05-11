import tkinter as tk
#fajl je isti kod
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
circle = canvas.create_oval(50, 50, 80, 80, outline="white", fill="blue")

def redraw():
    canvas.after(50, redraw)
    canvas.move(circle, 5, 5)
    if(canvas.coords(circle)[0] == 400):
        root.destroy()

redraw()
root.mainloop()