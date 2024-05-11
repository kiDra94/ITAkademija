#ppf ex 09 render.py
def render(h: int, w: int):
    for i in range(h):
        for j in range(w):
            print("#" if i==0 or j==0 or i==h-1 or j==w-1 else " ", end=" ")
        print("")
render(10,10)
render(3,6)