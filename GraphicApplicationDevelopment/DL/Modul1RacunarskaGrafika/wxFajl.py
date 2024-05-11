import wx 
  
app = wx.App() 
window = wx.Frame(None, title = "Hello World Window", size = (300,200)) 
label = wx.StaticText(window, label = "Hello World", pos = (100,50))
window.Show() 
app.MainLoop()