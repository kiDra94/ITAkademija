#Importujemo tkinter modul i skracujemo mu ime na tk
import tkinter as tk

#Pravimo prozor aplikacije
win = tk.Tk()
#Podesavamo velicinu prozora
win.minsize(300, 200)

#Pravimo labelu koju postavljamo da se nalazi na prozoru i postavljamo tekst labele i boju
#Pomocu grid modula postavljamo u kojoj koloni i kom redu ce se nalaziti labela
tk.Label(win,text = 'label1', bg = 'yellow').grid(column = 0, row = 0)
tk.Label(win,text = 'label2',bg = 'green').grid(column = 1, row = 1)
tk.Label(win,text = 'label3', bg = 'red').grid(column = 2, row = 2)
tk.Label(win,text = 'label4',bg = 'blue').grid(column = 3, row = 3)

#Smestamo u beskonacnu petlju aplikaciju kako se prozor ne bi zatvorio
win.mainloop()