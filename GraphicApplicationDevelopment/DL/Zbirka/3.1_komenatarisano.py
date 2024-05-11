#Importujemo tkinter modul
import tkinter as tk

#Pravimo prozor aplikacije
root = tk.Tk()

width=400
height=400

#Pravimo canvas objekat za definisanje objekata, odredjene visine i sirine
canvas=tk.Canvas(root,width=400,height=400)
#Postavljamo ga na ekran
canvas.pack()

#Pravimo liniju kojoj preciziramo  koordinate (x0, y0, x1, y1) odn. koordinate leve i desne tacke i boju 
line=canvas.create_line(100, 10, 300, 10,fill="red")

#Definisemo funkciju za pomeranje linije
def redraw():
    #Pomocu metode coords dobijamo koordinate objekta koji prosledimo a to je u ovom slucaju linija
    current_coords = canvas.coords(line)
    #Postavljamo uslov u kome pitamo da li je y koordinata linije veca ili jednaka od definisete visine prozora
    if (current_coords[1]>=height):
            #Ako je uslov tacan posle 1 milisekunde zatvaramo program
            root.after(1, root.destroy)
    #Pomeramo objekat line tako sto menjamo x i y koordinatu
    #Povecamo samo y koordinatu tako da se linija pomera samo na dole
    canvas.move(line,0,5)

    #Posle 50 milisekundi ce se opet pozvati funkciju redraw
    canvas.after(50,redraw)
#Pozivamo funkciju tako da pocne pomeranje linije
redraw()

#Smestamo u beskonacnu petlju aplikaciju kako se prozor ne bi zatvorio
root.mainloop()
