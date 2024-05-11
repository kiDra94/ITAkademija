#Importujemo tkinter modul i skracujemo mu ime na tk
import tkinter as tk

#Pravimo prozor aplikacije
win = tk.Tk()
#Podesavamo velicinu prozora
win.minsize(300, 200)

#Pravimo labelu koju postavljamo da se nalazi na prozoru i postavljamo tekst labele
#Postavljamo side na LEFT tako da se labele nalaze jedne pored druge umesto jedna ispod druge
#Postavljamo fill na vrednost BOTH tako da labele zauzimaju celu sirinu kolone
tk.Label(win,text = 'labela1', bg = 'yellow').pack(expand=True,side = tk.LEFT,  fill = tk.BOTH)
tk.Label(win,text = 'labela2',bg = 'green').pack(expand=True,side = tk.LEFT, fill = tk.BOTH)
tk.Label(win,text = 'labela3',bg = 'blue').pack(expand=True,side = tk.LEFT, fill = tk.BOTH)

##Smestamo u beskonacnu petlju aplikaciju kako se prozor ne bi zatvorio
win.mainloop()
