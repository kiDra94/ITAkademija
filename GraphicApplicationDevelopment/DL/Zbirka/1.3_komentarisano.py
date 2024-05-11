#Importujemo modul
import wx 

#Kreiramo objekat aplikacije
app = wx.App() 
#Kreiramo prozor sa tekstom i dimenzijom
window = wx.Frame(None, title = "WxPython okvir", size = (500,300)) 
#Pravimo labelu sa definisanim tekstom i x i y koordinatama
label = wx.StaticText(window, label = "Pera Peric", pos = (200,200))
#Prikazujemo prozor metodom show
window.Show() 
#Smestamo u beskonacnu petlju aplikaciju kako se prozor ne bi zatvorio
app.MainLoop()
