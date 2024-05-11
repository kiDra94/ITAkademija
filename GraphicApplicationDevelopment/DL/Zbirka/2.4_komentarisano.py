#Importujemo tkinter modul i skracujemo mu ime na tk
import tkinter as tk

#Pravimo prozor aplikacije
win = tk.Tk()
#Podesavamo velicinu prozora
win.minsize(300, 200)


#Pravimo labelu koju postavljamo da se nalazi na prozoru, defnisemo boju labele
#Pomocu place modula postavljamo tacne koordinate koliko ce biti udaljena labela
tk.Label(win,text = 'label1', bg = 'red').place(y = 10, x = 20)
tk.Label(win,text = 'label2',bg = 'blue').place(y=10 , x = 150)

#Smestamo u beskonacnu petlju aplikaciju kako se prozor ne bi zatvorio
win.mainloop()
