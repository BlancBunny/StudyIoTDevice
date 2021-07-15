# QT Designer 연동　소스　
import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/mainWindow.ui', self)

        self.btnStart.clicked.connect(self.btnStart_Clicked)
        self.btnStop.clicked.connect(self.btnStop_Clicked)
    
    def btnStart_Clicked(self):
        print('시작했습니다！')
        self.lblResult.setText('시작했습니다！')
    
    def btnStop_Clicked(self):
        print('종료했습니다！')
        self.lblResult.setText('종료했습니다！')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    