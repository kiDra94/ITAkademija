import tkinter as tk
root=tk.Tk()
width=400
height=400
canvas=tk.Canvas(root,width=400,height=400)
canvas.pack()

kvadrat1=canvas.create_rectangle(0, 0, 100, 100, fill='blue', outline='blue')
kvadrat2=canvas.create_rectangle(300, 300,400,400, fill='red', outline='red')

def redraw():
    kordinate_kvadrata1 = canvas.coords(kvadrat1)
    kordinate_kvadrata2 = canvas.coords(kvadrat2)
    if (kordinate_kvadrata1[1] >= height or kordinate_kvadrata2[0]<=0):
            root.after(1, root.destroy)
    
    canvas.move(kvadrat1,2,2)
    canvas.move(kvadrat2, -2,-2)
            
    canvas.after(50,redraw)
   
    

redraw()
root.mainloop()

