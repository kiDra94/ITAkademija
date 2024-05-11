#Importujemo tkinter modul i skracujemo mu ime na tk
import tkinter as tk

#Pravimo prozor aplikacije
root_window = tk.Tk()
#Podesavamo velicinu prozora
root_window.minsize(500, 100) 
#Pravimo labelu koju postavljamo da se nalazi na prozoru i postavljamo tekst labele
label = tk.Label(root_window, text="Pera Peric")
#Prikazuje labelu na prozoru
label.pack()
##Smestamo u beskonacnu petlju aplikaciju kako se prozor ne bi zatvorio
root_window.mainloop()
