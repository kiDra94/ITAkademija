import tkinter as tk
  
root = tk.Tk()
  
WIDTH = 500
HEIGHT = 500
  
canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()

x1 = WIDTH / 2
y1 = HEIGHT / 2

text = canvas.create_text(x1, y1*2-20, text = "Use arrow keys to move")
#*2-20 je trai and error, da vidis kako dobro izgleda
image = canvas.create_rectangle(x1 -15, y1-15, x1+15, x1+15)
#-15 i +15 da bi bilo centrirano

def move(event):
    # print(event.keysym) # ispisujemo sta je na tastaturi kliknuto
    if event.keysym == "Left":
        current_coords = canvas.coords(image)
        # dobija se lista sa 4 koordinatae x1, y1, x2, y2
        if current_coords[0] <= 0:
            canvas.move(image, WIDTH, 0)
            #ako je ispod nule vraca ga na desnu stranu, da ne ispadne iz prozora
        else:
            canvas.move(image, -10, 0)
            #pomjera za 10px u lijevo

    if event.keysym == "Right":
        current_coords = canvas.coords(image)
        if current_coords[0] >= WIDTH:
            canvas.move(image, -WIDTH, 0)
            #ako ispadne desno iz prozora vraca ga skorz lijevo
        else:
            canvas.move(image, 10, 0)

    if event.keysym == "Up":
        current_coords = canvas.coords(image)
        if current_coords[1] <= 0:
            #prvi element je y koordinata
            canvas.move(image, 0, HEIGHT)
            #ako ispadne desno iz prozora vraca ga skorz lijevo
        else:
            canvas.move(image, 0, -10)
            #pomjera za 10px na gore; 0/0 je u gornjem lijevom cosku zato -

    if event.keysym == "Down":
        current_coords = canvas.coords(image)
        if current_coords[1] >= HEIGHT:
            canvas.move(image, 0, -HEIGHT)
        else:
            canvas.move(image, 0, 10)


root.bind("<KeyPress>", move)
root.mainloop()