# QT5 사용자　윈도우　구성　예제
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My QT5 Window")
        self.setGeometry(80, 80, 800, 600)
        self.setWindowIcon(QIcon('./image/chart.png'))

        #label add
        self.label = QLabel('메시지　： ', self)
        self.label.setGeometry(10, 10, 300, 20)
        
        #button add
        self.btn = QPushButton('Click', self)
        self.btn.move(10, 50)

        self.btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        self.label.clear()
        self.label.setText('메시지　： 버튼　클릭！')

app = QApplication(sys.argv)
# win = QWidget()
# win.show()
# label = QLabel("Hello QT5")
# label.show()

win = MyWindow()
win.show()
app.exec_()
