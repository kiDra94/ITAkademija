from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(400, 400, 500, 300)
win.setWindowTitle("Hello World")
lable = QLabel("Hello World", parent=win)

win.show()
app.exec_()