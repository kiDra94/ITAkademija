import wx 
app = wx.App() 
window = wx.Frame(None, title = "WxPython okvir", size = (500,300)) 
label = wx.StaticText(window, label = "Pera Peric", pos = (200,200))
window.Show() 
app.MainLoop()
