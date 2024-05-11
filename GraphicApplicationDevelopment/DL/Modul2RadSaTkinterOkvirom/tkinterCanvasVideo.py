from tkinter import *

win = Tk()
win.title("Canvas")
tk_canvas = Canvas(win, width=300, height=100)

tk_canvas.create_line(10, 20, 200, 20, width=5)
tk_canvas.pack()

tk_canvas1 = Canvas(win, width=300, height=300)
tk_canvas1.create_arc(50, 50, 200, 200, start=120, extent=270, fill="blue")
tk_canvas1.pack()


tk_canvas2 = Canvas(win, width=300, height=300)
oval_id = tk_canvas2.create_oval(50, 50, 200, 200, fill="blue", width=5, outline="red")
print(oval_id)
tk_canvas2.pack()

tk_canvas2.tag_bind(oval_id, "<Button>", lambda e: tk_canvas2.delete(oval_id))

win.mainloop()