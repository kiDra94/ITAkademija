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

#Pravimo kvadrat kome preciziramo  koordinate (x0, y0, x1, y1) odn. koordinate gornje leve i donje desne tacke i boju linije
kvadrat1=canvas.create_rectangle(0, 0, 100, 100, fill='blue', outline='blue')
kvadrat2=canvas.create_rectangle(300, 300,400,400, fill='red', outline='red')

#Definisemo funkciju za pomeranje kvadrata
def redraw():
    #Pomocu metode coords dobijamo koordinate objekta koji prosledimo a to je u ovom slucaju kvadrat
    kordinate_kvadrata1 = canvas.coords(kvadrat1)
    kordinate_kvadrata2 = canvas.coords(kvadrat2)
    
    #Postavljamo uslov u kome pitamo da li je y koordinata prvog kvadrata veca ili jednaka od definisete visine prozora
    #ili da li je x koordinata drugog kvadrata manja ili jednaka od 0
    if (kordinate_kvadrata1[1] >= height or kordinate_kvadrata2[0]<=0):
            #Ako je uslov tacan posle 1 milisekunde zatvaramo program
            root.after(1, root.destroy)
            
    
   
    #Pomeramo kvadrat1 tako sto menjamo x i y koordinatu, posto se ove povecavaju kvadrat ide dole desno
    canvas.move(kvadrat1,5,5)
    #Pomeramo kvadrat2 tako sto menjamo x i y koordinatu, posto se ove smanjuju kvadrat ide gore levo
    canvas.move(kvadrat2, -5,-5)

    canvas.after(50,redraw)

#Pozivamo funkciju tako da pocne pomeranje linije
redraw()

#Smestamo u beskonacnu petlju aplikaciju kako se prozor ne bi zatvorio
root.mainloop()

