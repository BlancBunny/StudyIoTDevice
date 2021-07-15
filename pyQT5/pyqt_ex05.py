#QT Designer naver API 연동
import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from naverSearch import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/naverSearch.ui', self)

        # 시그널　핸들러　설정
        self.btnSearch.clicked.connect(self.btnSearch_Clicked)
    
    def btnSearch_Clicked(self):
        api = naverSearch()
        jsonResult = []
        sNode = 'news'
        search_word = self.txtSearchWord.text()
        display = 100

        jsonSearch = api.getNaverSearchResult(sNode, search_word, 1, display)
        print(jsonSearch)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    
