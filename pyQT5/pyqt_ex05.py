#QT Designer naver API 연동
import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from naverSearch import *
import webbrowser

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/naverSearch.ui', self)

        # 이벤트　핸들러　설정
        self.btnSearch.clicked.connect(self.btnSearch_Clicked)
        self.tblResult.itemSelectionChanged.connect(self.tblResult_Selected)

    def makeTable(self, result):
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(2)
        self.tblResult.setRowCount(len(result))

        self.tblResult.setHorizontalHeaderLabels(['기사제목','뉴스링크'])

        n = 0
        for post in result:
            self.tblResult.setItem(n, 0, QTableWidgetItem(post['title']))
            self.tblResult.setItem(n, 1, QTableWidgetItem(post['originallink']))
            n += 1
        self.tblResult.setColumnWidth(0,350)
        self.tblResult.setColumnWidth(1,200)
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers)
    def tblResult_Selected(self):
        # QMessageBox.about(self, 'popup', '웹브라우저를　띄웁니다．')
        selected = self.tblResult.currentRow() # 현재　선택된　열의　인덱스
        url = self.tblResult.item(selected, 1).text()
        QMessageBox.about(self, 'url', url)

    def btnSearch_Clicked(self):
        api = naverSearch()
        jsonResult = []
        sNode = 'news'
        search_word = self.txtSearchWord.text()
        display = 100

        if len(search_word) == 0:
            QMessageBox.about(self, 'popup', '검색어를　입력하세요')
            return

        jsonSearch = api.getNaverSearchResult(sNode, search_word, 1, display)
        jsonResult = jsonSearch['items']
        print(len(jsonResult))
        self.stsResult.showMessage('검색결과　： {0}개'.format(len(jsonResult)))
        self.makeTable(jsonResult)
        # print(jsonSearch)
        # model = QtGui.QStandardItemModel()
        # self.lsvSearchResult.setModel(model)
        
        # for post in jsonResult:
        #     item = QtGui.QStandardItem(post['title'])
        #     model.appendRow(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    
