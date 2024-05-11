import tkinter as tk
from random import randint
  
root = tk.Tk()
  
WIDTH = 500
HEIGHT = 500

score = 0
elements = randint(8,20)
  
canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()
  
x1 = WIDTH / 2
y1 = HEIGHT / 2
  
text = canvas.create_text(x1, y1 * 2 - 20, text = "Use arrow keys to move")
image = canvas.create_rectangle(x1, y1, x1 + 15, y1 + 15)

score_string_var = tk.StringVar()
score_string_var.set("Score: {}".format(score))
 
score_lable = tk.Label(textvariable=score_string_var, font="Bold")
score_lable.pack()

def overlapping_helper():
    s = canvas.bbox(image)
    #vraca ntorku sa koordinatama image
    #print(s)
    overlapping_result = canvas.find_overlapping(s[0], s[1], s[2], s[3])
    #pokazuje idjeve elementa koji se preklapaju
    #print(overlapping_result)
    if len(overlapping_result) > 1:
        canvas.delete(overlapping_result[1])
        global score
        score += 1
        score_string_var.set("Score: {}".format(score))


def move(event):
    overlapping_helper()
    if event.keysym == "Left":
        current_coords = canvas.coords(image)
        if current_coords[0] <= 0:
            canvas.move(image, WIDTH, 0)
        else:
            canvas.move(image, -10, 0)
    elif event.keysym == "Right":
        current_coords = canvas.coords(image)
        if current_coords[0] >= WIDTH:
            canvas.move(image, -WIDTH, 0)
        else:
            canvas.move(image, 10, 0)
    elif event.keysym == "Up":
        current_coords = canvas.coords(image)
        if current_coords[1] <= 0:
            canvas.move(image, 0, HEIGHT)
        else:
            canvas.move(image, 0, -10)
         
    elif event.keysym == "Down":
        current_coords = canvas.coords(image)
        if current_coords[1] >= HEIGHT:
            canvas.move(image, 0, -HEIGHT)
        else:
            canvas.move(image, 0, 10)

def setup():
    for i in range(elements):
        random_color = get_random_color()
        x = randint(10, WIDTH-15)
        y = randint(10, HEIGHT-15) 
        distance = randint(5, 30)
        canvas.create_oval(x, y, x+distance, y+distance, fill=random_color)

def get_random_color():
    r = lambda: randint(0,255)
    return "#%02X%02X%02X" % (r(), r(), r())

setup()            
root.bind("<KeyPress>", move)
root.mainloop()