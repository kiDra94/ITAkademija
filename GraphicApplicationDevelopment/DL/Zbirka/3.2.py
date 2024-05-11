import tkinter as tk
 
root = tk.Tk()
 
WIDTH = 500
HEIGHT = 500
canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()
 
text = canvas.create_text(250, 250 * 2 - 20, text = "Input x and y coordinates")
image = canvas.create_rectangle(50, 50, 0, 0)

def movee():
    
    kordinate_kvadrata = canvas.coords(image)
    if (kordinate_kvadrata[0] >= WIDTH or kordinate_kvadrata[0]<0 or kordinate_kvadrata[1]>=HEIGHT or kordinate_kvadrata[1]<0):
            root.after(1, root.destroy)
            

    x1=int(input('Unesite x1 koordinatu:'))
    y1=int(input('Unesite y1 koordinatu:'))

    x2=int(input('Unesite x2 koordinatu:'))
    y2=int(input('Unesite y2 koordinatu:'))
    
    canvas.coords(image, x1,y1,x2,y2)
    canvas.after(50,movee)
    print(canvas.coords(image))

movee()
root.mainloop()
