from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
 
app = QApplication([])
win = QMainWindow()
win.setGeometry(150,250,300,200)
win.setWindowTitle("PyQt5 okvir")
label = QLabel('Pera Peric', parent = win)
win.show()    
app.exec_()
