import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)
# win = QWidget()
# win.show()
# label = QLabel("Hello QT5")
# label.show()

win = MyWindow()
win.show()
app.exec_()
