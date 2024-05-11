##Importujemo sve iz tkinter modula
from tkinter import *

#postavljamo brojac na 0
counter=0
#Definisemo funkciju tako sto joj prosledjujemo event tako da predstavlja dogadjaj
def mouse_click(event):
    #Definisemo pristup globalnoj promenljivi counter
    global counter
    #Ispisujemo vrednost promenljive counter
    print('Counter is ',counter)
    #Povecavamo vrednost promenljive counter za 1
    counter+=1


#Pravimo prozor aplikacije
window = Tk()
#Podesavamo velicinu prozora
window.minsize(300, 100)

#Pravimo labelu koju postavljamo da se nalazi na prozoru i definisemo tekst labele
label = Label( window, text="Click here")
#Prikazujemo labelu na stranici
label.pack()

#Definisemo da kada se klikne dvaput na labelu da se pozove funkcija mouse_click
#Za Windows
label.bind( "<Double-Button>", mouse_click)

#Za Linux
#label.bind( "<Double-Button-1>", mouse_click)

#Smestamo u beskonacnu petlju aplikaciju kako se prozor ne bi zatvorio
window.mainloop()
