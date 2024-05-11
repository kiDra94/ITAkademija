#Uvodimo klase za rad
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
 
#Konstruktoru klase QApplication() prosledjujemo praznu listu kao argument. 
app = QApplication([])

#Pravimo prozor
win = QMainWindow()
#Definisemo dimenzije prozora tako sto prosledjujemo x i y koordinate u odnosu gornju levu ivicu ekrana i željenu širinu i visinu prozora
win.setGeometry(150,250,300,200)
#Definisemo tekst prozora
win.setWindowTitle("PyQt5 okvir")
#Pravimo labelu sa tekstom koju postavljamo da bude na prozoru
label = QLabel('Pera Peric', parent = win)
#Predstavljamo prozor
win.show()    
#Pozivamo etodu exec_ kako se prozor ne bi zatvorio. Ova metoda postavlja aplikaciju u beskonacnu petlju
app.exec_()
