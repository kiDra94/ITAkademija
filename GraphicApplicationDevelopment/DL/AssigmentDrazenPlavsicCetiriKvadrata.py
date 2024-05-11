from tkinter import *
WIDTH = 500
HEIGHT = 500
root = Tk()
root.title("Assigment Drazen Plavsic")
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

x1 = WIDTH / 2
y1 = HEIGHT / 2

dole_lijevo = canvas.create_rectangle(x1-80, y1, x1, y1+80, fill="yellow", outline="yellow")
dole_desno = canvas.create_rectangle(x1, y1, x1+80, y1+80, fill="green", outline="green")
gore_lijevo = canvas.create_rectangle(x1-80, y1-80, x1, y1, fill="blue", outline="blue")
gore_desno = canvas.create_rectangle(x1, y1-80, x1+80, y1, fill="red", outline="red")

def redraw():
    canvas.after(20, redraw)
    canvas.move(dole_lijevo, -5, 5)
    canvas.move(dole_desno, 5, 5)
    canvas.move(gore_lijevo, -5, -5)
    canvas.move(gore_desno, 5, -5)
    if(canvas.coords(dole_lijevo)[0] == -100):
        root.destroy()
#stavio sam za destroy samo jedan objekat, zato sto se sinhronizovano krecu pa ne vidim svrhu da obracam paznju i na ostale


redraw()
root.mainloop()